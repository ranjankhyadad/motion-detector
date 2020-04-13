import cv2

img = cv2.imread("mountain.jpg",1)

resized_image = cv2.resize(img, (int(img.shape[1]/6), int(img.shape[0]/6)))
#(width,height)
cv2.imshow("Mountain", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("final.jpg",img)
