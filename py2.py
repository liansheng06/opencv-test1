import cv2
cai=cv2.imread("/home/ls06/音乐/妈的我好菜.png")
b=cai[:,:,0]
g=cai[:,:,1]
r=cai[:,:,2]
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
cv2.imshow("result",cai)
cv2.waitKey()
cv2.destroyAllWindows()