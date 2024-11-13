import cv2 as cv
import sys
import glob

images = glob.glob('./images/*.jpg')

for image in images:
    img=cv.imread(image,0)
    re=cv.resize(img,(200,200))
    cv.imshow('Hey',re)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite('resized_'+image+'.jpg',re)