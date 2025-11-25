import cv2
cai=cv2.imread("/home/ls06/音乐/妈的我好菜.png",0)
cv2.imshow("result",cai)
cv2.waitKey()
cv2.destroyAllWindows()