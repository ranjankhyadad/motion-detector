import cv2

video = cv2.VideoCapture(0)

first_frame = None

while True:
    check,frame = video.read()
    capture = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    gray = cv2.GaussianBlur(capture,(21,21),0)
    
    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame,gray) # absolute diff between arrays

    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #threshold of the delta frame is set to 30-- any difference above 30 is white (255), else black (0)
    #Only second element need to be accessed. First element of the tuple is just a threshold value (30)

    threshold_frame = cv2.dilate(threshold_frame, None, iterations= 3)
    #dilate to smoothen the image

    (contours,_) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour)< 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 3)

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", threshold_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()