import pytesseract
import cv2
from PIL import Image
import os

img = cv2.imread('./files/14430267975121.jpg')
custom_config = r'-l spa --oem 3 --psm 11'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(img, config=custom_config, lang="ssq")
print(text)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
