# 用电脑自带的摄像头实现人脸导入
import cv2
# 摄像头
cap = cv2.VideoCapture(0)

flag = 1
num = 1
while cap.isOpened():
    ret_flag, frame = cap.read()
    cv2.imshow('Pic_Capture', frame)
    k = cv2.waitKey(1) & 0xFF
    # 按下按键S进行保存,按下按键Q退出
    if k == ord('s'):
        cv2.imwrite("D:/my_picture/"+str(num)+".HanXW"+".jpg", frame)
        print("Success to save picture "+str(num))
        print("——————————————")
        num += 1
    elif k == ord('q'):
        break
# 释放摄像头与释放内存
cap.release()
cv2.destroyAllWindows()
