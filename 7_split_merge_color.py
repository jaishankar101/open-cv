import cv2 as cv

img = cv.imread("images/dog.jpeg")

# # splits the image into B,G and R
# blue,green,red=cv.split(img) 
# cv.imshow("blue",blue)
# cv.imshow("green",green)
# cv.imshow("red",red)


# mergge the individual colors
mergerd_img=cv.merge()


 

# cv.imshow("dog",img)
cv.waitKey(0)