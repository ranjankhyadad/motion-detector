import cv2 as cv
import glob

images = glob.glob("*.jpg")
for image in images :
    img = cv.imread(image,0)
    resized_img = cv.resize(img,(100,100))
    cv.imshow("Resized Image",resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows
