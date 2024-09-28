### 1. Code Repository

**Repository Structure**:
```
livestream-app/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── uploads/               # Directory for uploaded images
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── OverlayControl.js # Overlay control component
│   │   ├── App.js             # Main React application
│   │   ├── App.css            # CSS styles
│   ├── package.json            # Frontend dependencies
├── README.md                  # General information about the project
```

### 2. API Documentation

**API Endpoints**:

#### Base URL
```
http://localhost:5000
```

#### 1. Create Overlay
- **Endpoint**: `/overlay`
- **Method**: `POST`
- **Request Body**: 
  ```json
  {
    "text": "Overlay Text",
    "x": 100,
    "y": 150,
    "file": null, // Optional for logo overlay
    "playing": false, // Optional, default is false
    "volume": 0.5 // Optional, default is 0.5
  }
  ```
- **Response**:
  ```json
  {
    "message": "Overlay created",
    "overlay": {
      "_id": "overlay_id",
      "text": "Overlay Text",
      "x": 100,
      "y": 150,
      "file": null,
      "playing": false,
      "volume": 0.5
    }
  }
  ```

#### 2. Retrieve Overlays
- **Endpoint**: `/overlay`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "_id": "overlay_id",
      "text": "Overlay Text",
      "x": 100,
      "y": 150,
      "file": null,
      "playing": false,
      "volume": 0.5
    }
  ]
  ```

#### 3. Update Overlay
- **Endpoint**: `/overlay/<overlay_id>`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "text": "Updated Overlay Text",
    "x": 120,
    "y": 160,
    "file": null, // Optional for logo overlay
    "playing": true, // Optional
    "volume": 0.8 // Optional
  }
  ```
- **Response**:
  ```json
  {
    "message": "Overlay updated"
  }
  ```

#### 4. Delete Overlay
- **Endpoint**: `/overlay/<overlay_id>`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
    "message": "Overlay deleted"
  }
  ```

### 3. User Documentation

**Setting Up the App**:

#### Prerequisites
- Python 3.x
- Node.js and npm

#### Backend Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/livestream-app.git
   cd livestream-app/backend
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**:
   ```bash
   python app.py
   ```

   The backend should now be running on `http://localhost:5000`.

#### Frontend Setup
1. **Navigate to the Frontend Directory**:
   ```bash
   cd ../frontend
   ```

2. **Install Frontend Dependencies**:
   ```bash
   npm install
   ```

3. **Run the React Application**:
   ```bash
   npm start
   ```

   The frontend should now be accessible at `http://localhost:3000`.

**Using the App**:

1. **Inputting the RTSP URL**:
   - Open the app in your browser.
   - In the input field labeled "Enter HTTP Stream URL", enter the RTSP URL for the live stream you want to play (e.g., `rtsp://your-stream-url`).

2. **Managing Overlays**:
   - **Adding Overlays**:
     - Choose between "Text Overlay" or "Logo Overlay" using the dropdown.
     - For a text overlay, input the desired text and specify its X and Y position.
     - For a logo overlay, click the file input to upload an image and specify its X and Y position.
     - Click "Add Overlay" to add it to the stream.
   
   - **Editing Overlays**:
     - Click on an existing overlay to select it for editing.
     - Update the text, position, or upload a new file as necessary.
     - Click "Update Overlay" to save changes.

   - **Deleting Overlays**:
     - Click the "X" button on an overlay to delete it.

### 4. README.md

You can create a `README.md` file at the root of your repository with the following content:

```markdown
# Livestream App

This application allows users to play live streams with overlay capabilities. Users can add text and logo overlays, which can be dragged and dropped on the video.

## Features

- Stream live video using an RTSP URL
- Add, edit, and delete overlays (text and images)
- Control playback (play, pause) and adjust volume

## Prerequisites

- Python 3.x
- Node.js and npm

## Setup Instructions

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/livestream-app.git
   cd livestream-app/backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

   frontend code is here https://github.com/Chirag-S-Kotian/frontend.git

2. Install frontend dependencies:
   ```bash
   npm install
   ```

3. Run the React application:
   ```bash
   npm start
   ```

## Usage Instructions

1. Input the RTSP URL for the live stream.
2. Manage overlays through the interface (add, edit, delete).
