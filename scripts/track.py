import numpy as np
import cv2

# Use this script to get proper object color

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
# Make a window for the video feed  
cv2.namedWindow('frame', cv2.CV_WINDOW_AUTOSIZE)

# Make the trackbar used for HSV masking    
cv2.createTrackbar('R','frame',0,255,nothing)
cv2.createTrackbar('G','frame',0,255,nothing)
cv2.createTrackbar('B','frame',0,255,nothing)

cv2.createTrackbar('Ru','frame',0,255,nothing)
cv2.createTrackbar('Gu','frame',0,255,nothing)
cv2.createTrackbar('Bu','frame',0,255,nothing)

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Name the variable used for mask bounds
    r = cv2.getTrackbarPos('R','frame')
    g = cv2.getTrackbarPos('G','frame')
    b = cv2.getTrackbarPos('B','frame')
    ru = cv2.getTrackbarPos('Ru','frame')
    gu = cv2.getTrackbarPos('Gu','frame')
    bu = cv2.getTrackbarPos('Bu','frame')
    print r,g,b
    print ru,gu,bu

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of color in HSV
    lower = np.array([b,g,r])
    upper = np.array([bu,gu,ru])

    # Threshold the HSV image to get only selected color
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask the original image
    res = cv2.bitwise_and(frame,frame, mask=mask)

    # Display the resulting frame
    cv2.imshow('frame',res)

    # Press q to quit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()