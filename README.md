# Parking Spot Detection Backend

This repository contains the backend for a parking spot detection platform. It uses FastAPI, YOLOv8, and OpenCV to detect vehicles in real-time and identify available parking spaces.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/parking-spot-detection-backend.git
   cd parking-spot-detection-backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Deployment

This application is configured for deployment on Render. Make sure to add the required files and environment variables.

## Endpoints

- `POST /detect_vehicles/`: Capture a frame from the camera and detect vehicles and parking spaces.
- `GET /closest_parking_space/`: Get the closest available parking space.
