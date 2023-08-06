import cv2 as cv
import numpy as np

img = cv.imread("images/dog.jpeg")

# # translation:-moves the image based on the specified scale of x and y using wrapAffine
# def translate(img,x,y):
#     transmatrix=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(img.shape[0],img.shape[1])
#     return cv.warpAffine(img,transmatrix,dimensions)

# # x=+ve => right else left
# # y=+ve => dowm else up

# translated_img=translate(img,-100,-100)
# cv.imshow("tranlated_img",translated_img)



# # rotation
# def rotation(img,angle,origin=None):
#     (height,width)=img.shape[:2]
#     if origin is None:
#         origin=(height//2,width//2)
#     rotate=cv.getRotationMatrix2D(origin,angle,1.0)
#     if angle==90:
#         dimensions=(width,height)
#     else:
#         dimensions=(height,width)
#     return cv.warpAffine(img,rotate,dimensions)

# rotated_img=rotation(img,60)
# cv.imshow("rotated_image",rotated_img)



# # flip the image verically(1) Or horizontally(0) or both(-1)
# flipped_img=cv.flip(img,-1)
# cv.imshow("flipped image",flipped_imgs)



# cv.imshow("dog",img)
cv.waitKey(0)