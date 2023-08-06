import cv2 as cv

img = cv.imread("images/dog.jpeg")

# # BGR to grayscale image
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray img",gray)
# re_img=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
# cv.imshow("re img",re_img)


# # BGR to HSV
# hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("hsv img",hsv_img)


# # BGR to LAB
# lab_img=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("lab img",lab_img)
# re_img=cv.cvtColor(lab_img,cv.COLOR_LAB2BGR)
# cv.imshow("re img",re_img)

# # BGR to RGB
# rgb_img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("rgb img",rgb_img)


# cv.imshow("dog",img)
cv.waitKey(0)