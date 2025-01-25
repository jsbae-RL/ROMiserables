import cv2              #opencv
import threading        #thread 분할 (webcam streamming 중에 반복문으로 프레임을 읽어와서 보여줘야하는데 다른작업도 해야해서 들고옴)


class VideoPlayer:
    def __init__(self):
        self.file_address = 'C:/ROKEY/ROMiserables/ROMiserables/03151_minsuje/hw/week2(py)/CCTV_project/CCTV_minsuje/src/recorder/cctv_recorded/'
        self.capture = None
        self.video_play_thread = None
        self.is_playing = False
        self.allowed_formats = ['mp4', 'mkv', 'mov','avi']

    def open_video_file(self, file_name):
        """비디오 파일을 열어 재생하는 함수."""
        # 파일 형식 확인
        if not any(file_name.endswith(fmt) for fmt in self.allowed_formats):
            print(f"지원되지 않는 파일 형식입니다: {file_name}")
            return

        # 비디오 파일 읽기 없으면 return
        self.capture = cv2.VideoCapture(self.file_address+file_name)
        if not self.capture.isOpened():
            print("비디오 파일을 열 수 없습니다.")
            return

        # 재생중 플래그 및 쓰래드 시작
        self.is_playing = True
        self.video_play_thread = threading.Thread(target=self._play_video)
        self.video_play_thread.start()

    def _play_video(self):
        while self.is_playing:
            ret, frame = self.capture.read()
            if not ret:
                print("비디오 끝.")
                break

            # 비디오 피드를 화면에 표시
            cv2.imshow('Video Playback', frame)

            # 'ESC'를 눌러 종료
            if cv2.waitKey(1) & 0xFF == 27:  # ESC 키 코드
                self.is_playing = False
                break
        self.release_resources()

    def release_resources(self):
        """비디오 자원 해제."""
        self.is_playing = False
        if self.capture:
            self.capture.release()
        cv2.destroyAllWindows()

    def stop_video(self):
        """비디오 재생 중지."""
        self.is_playing = False
        if self.video_play_thread and self.video_play_thread.is_alive():
            self.video_play_thread.join()

# play_cam = VideoPlayer()
# play_cam.open_video_file("")
# play_cam._play_video()
# play_cam.release_resources()
# play_cam.stop_video()