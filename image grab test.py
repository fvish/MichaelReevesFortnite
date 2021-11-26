from PIL import Image, ImageGrab
import numpy as np
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


while (True):
    im2 = ImageGrab.grab(bbox=(1240, 1535, 1298, 1565))
    img = np.array(im2)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    print(text)
    cv2.imshow(gray)
    key = cv2.waitKey(1)
    # kill key
    if key == 81 or key == 113:
        break
