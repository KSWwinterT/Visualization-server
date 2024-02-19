import numpy as np
from flask import Flask, Response, render_template
import serial
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('serial.js')

# 시리얼 포트 설정
ser = serial.Serial(
    port='/dev/ttyUSB0', # 연결된 시리얼 포트 번호
    baudrate=9600, # 통신 속도
    timeout=1 # 타임아웃 시간
)

# 영상 스트리밍 함수
def video_stream():
    while True:
        # 시리얼 포트로부터 데이터를 읽음
        data = ser.read(921600) # 640x480x3 크기의 영상 데이터
        if data:
            # 데이터를 numpy 배열로 변환
            frame = np.frombuffer(data, dtype=np.uint8)
            # 배열의 모양을 영상의 크기와 채널에 맞게 변경
            frame = frame.reshape(480, 640, 3)
            # 영상을 jpg 형식으로 인코딩
            ret, buffer = cv2.imencode('.jpg', frame)
            # 인코딩된 영상을 바이트로 변환
            frame = buffer.tobytes()
            # 바이트로 변환된 영상을 multipart 형식으로 전송
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_stream')
def index():
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', threaded=True, use_reloader=False)
