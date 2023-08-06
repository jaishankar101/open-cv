import cv2 as cv
import numpy as np

img = cv.imread("images/dog.jpeg")

# # image RGB(stored as BGR) to GrayScape
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Dog",gray)
# color=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
# cv.imshow("Dog",color)



# # blurring am image
# blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("Dog",blur)


# # use canny to get the edges in the image//Edge Cascade [Note:Rerduce the no of edges by using a slight blur]
# canny=cv.Canny(img,125,175)
# cv.imshow("Dog",canny)


# # dilation:Dilation adds pixels to the boundaries of objects in an image [prerequesit:canny image]
# canny=cv.Canny(img,125,175)
# for i in range(10):
#     dilate=cv.dilate(canny,(7,7),iterations=i)
#     cv.imshow("dialated Dog canny",dilate)
#     cv.waitKey(0)


# # Eroding : opposite of dialation i.e  erosion removes pixels on object boundaries
# canny=cv.Canny(img,125,175)
# eroded=cv.erode(canny,(7,7),iterations=4)
# cv.imshow("eroded image",eroded)


# # resize  an image[(INTER_AREA=to reduce the size),(INTER_LINEAR,INTER_CUBIC(slower but better)=to increase the size)]
# resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized Image",resized)


# # crop the image
# cropped=img[50:200,40:200]
# cv.imshow("cropped image",cropped)



# cv.imshow("Dog",img)
cv.waitKey(0)