from kraken.rpred import rpred
import cv2

img = cv2.imread('files/1366_521.jpg', cv2.IMREAD_GRAYSCALE)
result = rpred(img)
print(result)