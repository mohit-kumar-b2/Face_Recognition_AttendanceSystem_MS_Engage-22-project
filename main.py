from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from time import strftime
from datetime import datetime


class Face_Recognition_Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        img=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\college.jpg")
        img=img.resize((400,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=100)


        img1=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\face recogno.jpg")
        img1=img1.resize((480,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=480,height=100)


        img2=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\college image.jpg")
        img2=img2.resize((400,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=880,y=0,width=400,height=100)


        #background image
        img3=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\website-background-image-size-psd-vector-photo.jpg")
        img3=img3.resize((1280,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1280,height=600)



        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="orange")
        title_lbl.place(x=0,y=0,width=1280,height=40)



        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",13,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,height=40)
        time()


        #first button
        img4=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\student details.jpg")
        img4=img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand1")
        b1.place(x=160,y=60,width=180,height=180)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand1",font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=160,y=241,width=180,height=30)


        #second button
        img5=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\heading.jpg")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand1",command=self.face_data)
        b1.place(x=550,y=60,width=180,height=180)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand1",command=self.face_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=550,y=241,width=180,height=30)
        


        #third button
        img6=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\attendance.png")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand1",command=self.attendance_data)
        b1.place(x=940,y=60,width=180,height=180)

        b1_1=Button(bg_img,text="Attendance",cursor="hand1",command=self.attendance_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=940,y=241,width=180,height=30)



        #fourth button
        img7=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\training.png")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand1",command=self.train_data)
        b1.place(x=160,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Train Data",cursor="hand1",command=self.train_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=160,y=531,width=180,height=30)



        #fifth button
        img8=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\photos.jpg")
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand1",command=self.open_img)
        b1.place(x=550,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Registered Faces",cursor="hand1",command=self.open_img,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=550,y=531,width=180,height=30)



        #sixth button
        img9=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\exit.jpg")
        img9=img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand1",command=self.iExit)
        b1.place(x=940,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Exit",cursor="hand1",command=self.iExit,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=940,y=531,width=180,height=30)



    def open_img(self):
        os.startfile("data")



    #Function Buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)



    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)



    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
    






if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_Attendance(root)
    root.mainloop()