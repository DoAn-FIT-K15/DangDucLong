import numpy as np
import cv2
import time
import os
from tkinter import *
# Label: 00000 là ko cầm tiền, còn lại là các mệnh giá
label = "600000"

cap = cv2.VideoCapture(0)

# Biến đếm, để chỉ lưu dữ liệu sau khoảng 60 frame, tránh lúc đầu chưa kịp cầm tiền lên
def makedata():
    i=0
    while(True):
    # Capture frame-by-frame
    #
        i+=1
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.resize(frame, dsize=None,fx=0.3,fy=0.3)

    # Hiển thị
        cv2.imshow('frame',frame)

    # Lưu dữ liệu
        if i>=60 and i<=1060:
            print("Số ảnh capture = ",i-60)
        # Tạo thư mục nếu chưa có
            if not os.path.exists('data/' + str(label)):
                os.mkdir('data/' + str(label))

            cv2.imwrite('data/' + str(label) + "/" + str(i) + ".png",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return

window = Tk()
window.geometry("680x640")
photo2=PhotoImage(file='button.png')
button=Button(window,text="Begin!!",command=makedata,font=("Comic Sans",30),image=photo2,compound='left')
button.pack()
button.place(x=250,y=270)
label3=Label(window,text="Make Data For Model",font=('Arial',30))
label3.place(x=150,y=200)
photo3=PhotoImage(file='door.png')
button2=Button(window,text="Close",command=window.destroy,font=("Comic Sans",30),image=photo3,compound='left')
button2.pack()
button2.place(x=260,y=350)
photo = PhotoImage(file='camera.png')
label1 = Label(window,text="Nhan dang tien VN",font=('Arial',40,'bold'),
            fg = 'green', relief=RAISED, bd=5, padx=10, pady=10, image = photo, compound = 'bottom')
label1.place(x=100,y=10)
label2=Label(window,text="An 'q' de dung camera",font=('Arial',40,'underline'))
label2.place(x=100,y=450)
window.mainloop()
# When everything done, release the capture
