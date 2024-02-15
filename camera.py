import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read() # yolo 영상 추가 부분
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()