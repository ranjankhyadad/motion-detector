import cv2

video = cv2.VideoCapture(0)
# 0 and 1 for cameras and path for video file
frame_rate = 0

while True:
    frame_rate = frame_rate+1
    check,frame = video.read()
    capture = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    #convert color
    cv2.imshow("Capture", capture)
    
    key = cv2.waitKey(1)
    if key == ord("c"):
        break

print(frame_rate)
video.release()
cv2.destroyAllWindows()