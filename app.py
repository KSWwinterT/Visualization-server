# from flask import Flask, jsonify, render_template
# import cv2
# import numpy as np
# from darknet import darknet  # YOLO 관련 모듈 임포트
#
# app = Flask(__name__)
#
# # YOLO 초기화
# net, meta = darknet.load_net("yolov5.cfg", "yolov5.weights", 0)
# darknet_image = darknet.make_image(darknet.network_width(net), darknet.network_height(net), 3)
#
# # 웹캠 초기화 (예시로 0번 웹캠 사용)
# cap = cv2.VideoCapture(0)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/get_detection_count')
# def get_detection_count():
#     ret, frame = cap.read()
#
#     # YOLO 입력 형식으로 변환
#     darknet.copy_image_from_bytes(darknet_image, frame.tobytes())
#
#     # YOLO 객체 탐지 수행
#     detections = darknet.detect_image(net, meta, darknet_image)
#
#     # 여기에서 디텍션 결과를 가지고 원하는 로직을 수행하고, 사람 수 등을 얻을 수 있습니다.
#     person_count = len([obj for obj in detections if obj[0] == 'person'])
#
#     return jsonify({'person_count': person_count})
#
# if __name__ == '__main__':
#     app.run(debug=True)
