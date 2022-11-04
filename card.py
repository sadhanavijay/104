import cv2
poster=cv2.imread("poster.jpg")
rocket=poster[120:360,400:500]
poster[0:240,500:600]=rocket
text_to_show="I <3 coding at whjr"
cv2.putText(poster,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
cv2.imshow("display image",poster)
cv2.waitKey(0)