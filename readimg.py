from cgitb import grey
import cv2
img=cv2.imread("butterfly.jpg")
cv2.imshow("display image",img)
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("display image",gray_img)
print(gray_img)
cv2.waitKey(0)
