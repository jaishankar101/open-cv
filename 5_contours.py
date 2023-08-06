import cv2 as cv

img = cv.imread("images/dog.jpeg")

# Contours can be explained simply as a curve 
# joining all the continuous points (along the boundary),
#  having same color or intensity. 
# The contours are a useful tool for shape analysis
#  and object detection and recognition.

# gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# canny_img=cv.Canny(img,125,175)
# contours,heirarchies=cv.findContours(canny_img,cv.RETR_TREE,
#                                      cv.CHAIN_APPROX_SIMPLE)


# cv.imshow("dog",canny_img)


# # NOTE:threshold if val<125 0 else 1
# ret,thresh=cv.threshold(gray_img,125,255,cv.THRESH_BINARY)
# cv.imshow("threshhold img",thresh)
# cv.waitKey(0)

import numpy as np
# # drawing contours on a blank image
# blank=np.zeros(img.shape,"uint8")
# cv.drawContours(blank,contours,-1,(0,255,0),1)
# cv.imshow("drawing of contours",blank)
cv.waitKey(0)
