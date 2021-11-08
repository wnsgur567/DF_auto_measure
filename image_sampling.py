# pip install pyautogui
# pip install mss
# mss 는 screenshot을 위해
# pip install opencv-python
# pip install numpy

import pyautogui
import mss
from cv2 import cv2
import numpy as np


# while True:
#     x, y = pyautogui.position()
#     position_str = 'X: ' + str(x) + ' Y: ' + str(y)
#     print(position_str)


def get_mouse_pos():
    return pyautogui.position()


# capture 된 이미지를 return
def capture_img(x: int, y: int, w: int, h: int):
    # image 캡쳐
    with mss.mss() as sct:
        _img = np.array(sct.grab(
            {'left': x, 'top': y, 'width': w, 'height': h}
        ))
        return _img


#  아래 내일 할 것들
origin_image = [cv2.imread('읽어올 원본 이미지들...')]

# 캡쳐된 이미지
img = capture_img(1000, 200, 300, 300)
# 캡쳐사진 확인
cv2.imshow('captured image', img)
cv2.waitKey(0)

# https://bkshin.tistory.com/entry/OpenCV-12-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9C%A0%EC%82%AC%EB%8F%84-%EB%B9%84%EA%B5%90-%EC%82%AC%EB%9E%8C-%EC%96%BC%EA%B5%B4%EA%B3%BC-%ED%95%B4%EA%B3%A8-%ED%95%A9%EC%84%B1-%EB%AA%A8%EC%85%98-%EA%B0%90%EC%A7%80-CCTV

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 캡쳐된 이미지와 원본들과 비교
for ori in origin_image:
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
    # 실제 비교 알고리즘 계산
    ret = cv2.compareHist(img, hist, cv2.HISTCMP_CORREL)
    print("일치율 : {0}".format(ret))
