import cv2 as cv
import numpy as np


# img = cv.imread("images/dog.jpeg")
# cv.imshow("doggy",img)


# #blank image
blank = np.zeros((500,500,3),dtype="uint8")

# # all green
# blank[:]=0,0,200

# # get a hollow rectangle with  border of certain thickness
# cv.rectangle(blank,(0,0),(300,350),(20,30,40),thickness=3)

# # get a filled recrtangle by using thickness=cv.FILLED (or) -1
# cv.rectangle(blank,(0,0),(300,350),(200,0,0),thickness=cv.FILLED)


# # to drar a circle
# cv.circle(blank,(250,350),23,(3,200,4),thickness=cv.FILLED)

# # draw the line
# cv.line(blank,(200,200),(300,300),(200,0,0),thickness=3)

# # write text into the image 
# cv.putText(blank,"this is text",(250,250),cv.FONT_HERSHEY_TRIPLEX,1.2,(200,0,0),thickness=2)

cv.imshow("blank",blank)
cv.waitKey(0)