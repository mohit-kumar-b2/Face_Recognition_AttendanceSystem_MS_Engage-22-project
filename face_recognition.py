from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")



        title_lbl=Label(self.root,text="FACE  RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=40)

        img_top=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\faced1.jpg")
        img_top=img_top.resize((1280,660),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        bg_img=Label(self.root,image=self.photoimg_top)
        bg_img.place(x=0,y=40,width=1280,height=660)


        b1_1=Button(bg_img,text="FACE RECOGNITION",cursor="hand1",command=self.face_recog,font=("times new roman",25,"bold"),bg="red",fg="white")
        b1_1.place(x=450,y=580,width=372,height=42)




    #attendance
    def mark_attendance(self,i,r,n,d):
        with open("AttendanceSheet/Mohit.csv","r+",newLine="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")





    # face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where student_id"+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                


                my_cursor.execute("select student_id from student where student_id"+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                


                if confidence>77:
                    cv2.putText(img,f"Student Id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                    self.mark_attendance(i,n)
                    

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,25,255),1)

                coord=[x,y,w,y]

            return coord


        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()  