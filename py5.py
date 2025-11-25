import cv2
cai=cv2.imread("/home/ls06/音乐/妈的我好菜.png")
height,width=cai.shape[:2]
M=cv2.getRotationMatrix2D((width/2,height/2),45,1)
cai=cv2.warpAffine(cai,M,(width,height))
cv2.imshow("result",cai)
cv2.waitKey()
cv2.destroyAllWindows()