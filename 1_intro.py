import cv2 as cv

# reading and displaing image

# resimg=cv.imread('C:/Users/Jai Shankar/OneDrive/Pictures/D4120.jpg')
# cv.imshow("Jai Shankar",resimg)
# cv.waitKey(0)





# reading and displaing videos

def rescaleFrame(frame,scale=0.75):
    
    resized_shape=(int(frame.shape[0]*scale),int(frame.shape[1]*scale))
    return cv.resize(frame,resized_shape,interpolation=cv.INTER_AREA)


resvid=cv.VideoCapture("C:/Users/Jai Shankar/OneDrive/Pictures/Camera Roll/WIN_20230609_17_25_34_Pro.mp4")
while True:
    isTrue,frame=resvid.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow("interview prep",frame)
    # cv.imshow("interview prep",frame_resized)
    if cv.waitKey(20) and 0xFF==ord('d'):
        break
# resvid.release()
# cv.destroyAllWindows()




