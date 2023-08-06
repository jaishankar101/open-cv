import cv2 as cv

img = cv.imread("images/dog.jpeg")

# splits the image into B,G and R
blue,green,red=cv.split(img) 
# cv.imshow("blue",blue)
# cv.imshow("green",green)
# cv.imshow("red",red)


# # merge the individual colors
# mergerd_img=cv.merge([blue,green,red])
# cv.imshow("merges image",mergerd_img)



# # to split the image as red,blue and greencomponents
# import numpy as np

# blank=np.zeros(img.shape[:2],dtype='uint8')

# blue_img=cv.merge([blue,blank,blank])
# green_img=cv.merge([blank,green,blank])
# red_img=cv.merge([blank,blank,red])

# cv.imshow("blue image",blue_img)
# cv.imshow("green image",green_img)
# cv.imshow("red image",red_img)






# cv.imshow("dog",img)
cv.waitKey(0)