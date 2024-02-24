import cv2 as cv
import numpy as np



img = cv.imread('images/dog.jpeg')
cv.imshow("dog",img)



blank=np.zeros(img.shape,'uint8')
cv.imshow("blank",blank)

mask=cv.circle(blank,(img.shape[0]//2,img.shape[1]//2),50,255,-1)
cv.imshow("mask",mask)


masked_img=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked image",masked_img)

cv.waitKey(0)