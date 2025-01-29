import cv2              #opencv
import threading        #thread 분할 (webcam streamming 중에 반복문으로 프레임을 읽어와서 보여줘야하는데 다른작업도 해야해서 들고옴)
os sys

from recorder.video_player import VideoRecorder

class WebCamStreamer():
    def __init__(self,cam_num=0):   # 노트북은 캠이 기본 탑재 되어있어서 그냥 아무것도 선택안하면 노트북 웹캠 자체그대로로
        self.selected_cam_number = cam_num
        self.capture = None
        self.stream_thread = None
        self.is_streamming = False
        #self.recorder = VideoRecorder()
    
    def open_cam(self):
        self.capture = cv2.VideoCapture(self.selected_cam_number,cv2.CAP_DSHOW)
        if not self.capture.isOpened(): # 열려있는지 확인
            raise Exception("카메라가 연결되지 않아 스트리밍을 할 수 없습니다.")
        self.is_streamming = True       #스트리밍 상태가 True가 되야 스트리밍 함수 내부에 while로 돌릴수 있음.
        self.stream_thread = threading.Thread(target=self.cam_streamming)   #쓰레드 분할 타겟 스트림 함수
        self.stream_thread.start()      #스트림 스래드 활성화
    
    def cam_streamming(self):
        while self.is_streamming:
            ret, frame = self.capture.read()    #정보를 읽어와서
            if not ret:         #상태가 False이면 읽어올수 없는 상태임
                print("프레임을 읽을 수 없습니다. 다시 시도합니다....")
                continue
            # frame은 하나의 이미지임 그래서 cv2의 이미지를 읽어오는 imshow함수 사용
            cv2.imshow("streamming_On_Air...",frame)    
            # cv.waitkey는 입력 키의 값을 나타내는 정수를 반환하는데 
            # 비트 마스크 0xFF로 받은 키 값의 하위 8비트만 확인한다
            # 27번은 esc키의 입력값이고 해당 값이 들어오면 스트리밍을 종료한다.
            key = cv2.waitKey(1)&0xFF
            if key==27:
                break
            # if key== ord('r'):
            #     if self.recorder.recording==False:
            #         video_frame_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            #                       int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            #         self.recorder.open_video_record(video_frame_size)
            #         self.is_streamming = True
            #     else:
            #         self.recorder.stop_recording()
            #         self.is_recording = False
            #         print("녹화 중지!")
        self.close_stream_resources()
        # if self.recorder.recording:
        #     self.recorder.stop_recording()
        #     self.is_recording = False
        #     print("녹화 중지!")

    def close_ALL_resources(self):
        self.close_stream_resources()
        self.close_thread_resources()

    def close_thread_resources(self):
        if self.stream_thread and self.stream_thread.is_alive():
            self.stream_thread.join()  # 스레드가 종료될 때까지 기다림

    def close_stream_resources(self):
        if self.capture:
            self.capture.release()  # 연결 해제
        cv2.destroyAllWindows()     # opencv로 연 모든 윈도우창 닫기
        self.is_streamming = False

play_cam = WebCamStreamer()
play_cam.open_cam()
play_cam.cam_streamming()
play_cam.close_ALL_resources()