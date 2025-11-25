import cv2
import numpy as np
cai=cv2.imread("/home/ls06/音乐/妈的我好菜.png")
cai1=cai
cai=cv2.cvtColor(cai,cv2.COLOR_BGR2GRAY)
ret,cai=cv2.threshold(cai,187,255,cv2.THRESH_BINARY)
for i in range(447):
    for j in range(992):
        if cai[i,j]==255:
            cai[i,j]=0
        else:
            cai[i,j]=255
cole=np.ones((40,40),np.uint8)
big=cv2.dilate(cai,cole)
contours,_=cv2.findContours(big,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cai1=cv2.drawContours(cai1,contours,-1,(0,0,255),6)
cv2.imshow("aa",cai1)
cv2.waitKey()
cv2.destroyAllWindows()