from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import os
import logging

app = Flask(__name__)
CORS(app)

# MongoDB configuration
client = MongoClient("mongodb+srv://ck17:chirag123@flask1.cjipb.mongodb.net/?retryWrites=true&w=majority&appName=flask1")
db = client['flask1']
overlays_collection = db['overlays']

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Logging configuration
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return "Livestream App Backend is running."

# Endpoint to upload an image overlay
@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        image = request.files['image']
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        return jsonify({"message": "Image uploaded successfully", "path": image_path})
    except Exception as e:
        logging.error(f"Error uploading image: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# CRUD API for overlays
@app.route('/overlay', methods=['POST'])
def create_overlay():
    try:
        overlay_data = request.json
        if not overlay_data:
            return jsonify({"error": "No data provided"}), 400

        # Add default values for playback control settings
        overlay_data['playing'] = overlay_data.get('playing', False)
        overlay_data['volume'] = overlay_data.get('volume', 0.5)

        result = overlays_collection.insert_one(overlay_data)
        overlay_data['_id'] = str(result.inserted_id)
        return jsonify({"message": "Overlay created", "overlay": overlay_data})
    except Exception as e:
        logging.error(f"Error creating overlay: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/overlay', methods=['GET'])
def get_overlays():
    try:
        overlays = list(overlays_collection.find())
        for overlay in overlays:
            overlay['_id'] = str(overlay['_id'])
        return jsonify(overlays)
    except Exception as e:
        logging.error(f"Error retrieving overlays: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/overlay/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    try:
        updated_data = request.json
        if not updated_data:
            return jsonify({"error": "No data provided"}), 400

        # Ensure we can update playback control settings
        if 'playing' in updated_data or 'volume' in updated_data:
            updated_data['playing'] = updated_data.get('playing', False)
            updated_data['volume'] = updated_data.get('volume', 0.5)

        result = overlays_collection.update_one({'_id': ObjectId(overlay_id)}, {'$set': updated_data})
        if result.matched_count > 0:
            return jsonify({"message": "Overlay updated"})
        else:
            return jsonify({"message": "Overlay not found"}), 404
    except Exception as e:
        logging.error(f"Error updating overlay with id {overlay_id}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/overlay/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    try:
        result = overlays_collection.delete_one({'_id': ObjectId(overlay_id)})
        if result.deleted_count > 0:
            return jsonify({"message": "Overlay deleted"})
        else:
            return jsonify({"message": "Overlay not found"}), 404
    except Exception as e:
        logging.error(f"Error deleting overlay with id {overlay_id}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
