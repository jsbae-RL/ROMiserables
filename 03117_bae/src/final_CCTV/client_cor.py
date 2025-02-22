# Client script to send webcam frames to the server
import cv2
import requests
import time

def send_webcam():
    url = "http://192.168.0.9:8000/track_objects"
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        files = {"file": buffer.tobytes()}
        response = requests.post(url, files=files)
        print(response.json())
        time.sleep(0.1)  # Send frames every 100ms
    cap.release()

if __name__ == "__main__":
    send_webcam()
