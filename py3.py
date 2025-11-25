import cv2
cai=cv2.imread("/home/ls06/音乐/妈的我好菜.png")
for i in range(447):
    for j in range(992):
        for k in range(3):
            if cai[i,j,k]==255:
                cai[i,j,k]=0
cv2.imshow("result",cai)
cv2.waitKey()
cv2.destroyAllWindows()