from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from ultralytics import YOLO
from collections import defaultdict
import uvicorn
import tempfile

app = FastAPI()

# Load YOLO model
model = YOLO("yolo11n.pt")

@app.post("/track_objects")
async def track_objects(file: UploadFile = File(...)):
    """Receives an image and returns object tracking data."""
    
    # Save uploaded file to a temporary location
    temp_image = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    temp_image.write(await file.read())
    temp_image.close()
    
    frame = cv2.imread(temp_image.name)
    track_history = defaultdict(list)
    
    results = model.track(frame, persist=True, classes=0, tracker='bytetrack.yaml')
    boxes = results[0].boxes.xyxy.cpu().tolist()
    track_ids = results[0].boxes.id.int().cpu().tolist()
    
    frame_data = []
    for box, track_id in zip(boxes, track_ids):
        x1, y1, x2, y2 = box
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        
        track_history[track_id].append((x_center, y_center))
        if len(track_history[track_id]) > 30:
            track_history[track_id].pop(0)
        
        frame_data.append({
            "track_id": track_id,
            "bounding_box": [x1, y1, x2, y2],
            "trajectory": track_history[track_id]
        })
    
    return {"tracking_data": frame_data}