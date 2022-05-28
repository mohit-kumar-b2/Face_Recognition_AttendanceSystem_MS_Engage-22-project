from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")



        title_lbl=Label(self.root,text="HELP  DESK",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=40)

        img_top=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\helpdesk.jpg")
        img_top=img_top.resize((1280,660),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        lbl=Label(self.root,image=self.photoimg_top)
        lbl.place(x=0,y=40,width=1280,height=660)



        email_frame=LabelFrame(lbl,bd=2,bg="white",fg="red",relief=RIDGE,text="Email: mohit.bittu.2001@gmail.com", font=("times new roman",25,"bold"))
        email_frame.place(x=390,y=270,width=530,height=40)







if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop() 
