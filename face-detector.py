import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

img1 = cv.imread("face.jpg")
gray_img = cv.imread("face.jpg",0)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)
# type of faces is ndarray - n dimensional numpy array
#scalefactor 1.05 means the window is downscaled by 5% everytime till it finds a face

for x,y,w,h in faces:
    img1 = cv.rectangle(img1, (x,y), (x+w, y+h), (255,255,255), 3)

resized = cv.resize(img1,(int(img1.shape[1]/3), int(img1.shape[0]/3)))
# print(faces)
cv.imshow("Updated", resized)
cv.waitKey(0)
cv.destroyAllWindows()