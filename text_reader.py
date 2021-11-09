# training tool 참고 주소 : https://blog.naver.com/PostView.nhn?blogId=beodeulpiri&logNo=221615329276
# tesseract 참고 주소 : https://m.blog.naver.com/hn03049/221957851802

# 바로 읽어내지 않고 영역을 잘라내서 그부분만 읽을 수 있도록
# string 의 크기는 20을 넘게 주면 더 잘 보일 수 있다 카더라
# 후처리는 여러종류 테스트 해보고 이미지로 띄워서 직접 확인해봐야 정확도를 올릴 수 있을 듯
# jTessBoxEditor 로 학습을 시켜봤는데 석 만족스러운 결과는 아니였다. 그래도 폰트 적용했을때 조금 더 정확도가 올라간거 같기도...

import pytesseract
from cv2 import cv2
import time



pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('ttttttt.png')
img_gray = cv2.imread('ttttttt.png',cv2.IMREAD_GRAYSCALE)

# 0 : legacy
# 2 : legacy + lstm
# 3 : default
config = '--oem 3'
text = pytesseract.image_to_string(img_gray, lang='kor',config= config  )

print(text)
