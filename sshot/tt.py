import cv2 as cv
img = cv.imread('p2.png')
cv.namedWindow("Image")
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
