import cv2 as cv


img=cv.imread("images/dog.jpeg")

# # using blur
# # we use the kernel(n,n) wnere we take the average of the values in the kernel and pass it to the middle position of the matrix
# # the kernel moves over the source image matrix.
# blur_img=cv.blur(img,(3,3))
# cv.imshow("blurred image",blur_img)
 


# # gaussian blur
# # same as blur but considers weights and is less blurred compared to basic blur.
# gaussian_blur_img=cv.GaussianBlur(img,(5,5),0)
# cv.imshow("Gaossian blur image",gaussian_blur_img)



# # median blur : used in advanced Cv as it is better banth others in noice reduction
# median_blur_img=cv.medianBlur(img,5)
# cv.imshow("median blur image",median_blur_img)



# # bilateral filter
# bilateral_img=cv.bilateralFilter(img,40,50,34)
# cv.imshow("bilateral image",bilateral_img)


cv.imshow("dog",img)
cv.waitKey(0)