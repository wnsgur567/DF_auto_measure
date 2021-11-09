import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
tt_img = Image.open('frame_img/test.png')

text = pytesseract.image_to_string(tt_img, lang='kor+eng')

print(text)
