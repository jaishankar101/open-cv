import cv2 as cv

img = cv.imread("images/dog.jpeg")

# splits the image into B,G and R
blue,green,red=cv.split(img) 
# cv.imshow("blue",blue)
# cv.imshow("green",green)
# cv.imshow("red",red)


# merge the individual colors
mergerd_img=cv.merge([blue,green,red])
cv.imshow("merges image",mergerd_img)


import numpy as np

blank=np.zeros(img.shape[2:],dtype='uint8')

 

# cv.imshow("dog",img)
cv.waitKey(0)