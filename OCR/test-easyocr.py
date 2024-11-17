import easyocr
import cv2

read = easyocr.Reader(['es'], gpu=False)
img = cv2.imread('files/1366_521.jpg')
#img = cv2.resize(img, (800, 600))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result = read.readtext(img, paragraph=False)

for res in result:
    print("res:",res)
    pt0 = tuple(res[0][0])
    pt1 = tuple(res[0][1])
    pt2 = tuple(res[0][2])
    pt3 = tuple(res[0][3])

    cv2.rectangle(img, pt0, pt2, (0, 255, 0), 2)
    cv2.putText(img, res[1], pt0, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()