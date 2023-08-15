import cv2 as cv
import numpy as np


blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),thickness=cv.FILLED,color=255)
cv.imshow("rectangle",rectangle)

circle=cv.circle(blank.copy(),(200,200),180,thickness=cv.FILLED,color=255)
cv.imshow("circle",circle)


# # performs bitwise and on the imput images:common region
# bitwise_and_img=cv.bitwise_and(rectangle,circle)
# cv.imshow("bitwise and image",bitwise_and_img)


# # performs bitwise or on the imput images:common+specific
# bitwise_or_img=cv.bitwise_or(rectangle,circle)
# cv.imshow("bitwise or image",bitwise_or_img)


# # xor
# bitwise_xor_img=cv.bitwise_xor(rectangle,circle)
# cv.imshow("bitwise xor image",bitwise_xor_img)

# # not
# bitwise_not_img=cv.bitwise_not(rectangle)
# cv.imshow("bitwise not image",bitwise_not_img)


cv.waitKey(0)