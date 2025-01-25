import cv2
import datetime

class VideoRecorder():
    def __init__(self):
        self.path_record_adress = "C:/ROKEY/ROMiserables/ROMiserables/03151_minsuje/hw/week2(py)/CCTV_project/CCTV_minsuje/src/recorder/cctv_recorded/"
        self.recording = None
    
    def open_video_record(self, frame_size):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f"{self.path_record_adress}CCTV_{timestamp}.avi"
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(str(file_name), fourcc, 20.0, frame_size)
        print(f"녹화 시작: {file_name}")
    
    def on_air_recording(self,frame):
        if self.recording:
            self.recording.write(frame)

    def stop_recording(self):
        if self.out:
            self.out.release()
            self.out = None
        print("녹화 중지 및 저장.")