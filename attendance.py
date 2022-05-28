from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import csv
from tkinter import filedialog
from help import Help

myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")



        #variables
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_attendance=StringVar()




        img=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\students2.jpg")
        img=img.resize((400,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=100)


        img1=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\students.jpg")
        img1=img1.resize((480,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=480,height=100)


        img2=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\students5.jpg")
        img2=img2.resize((400,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=880,y=0,width=400,height=100)


        img3=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\website-background-image-size-psd-vector-photo.jpg")
        img3=img3.resize((1280,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1280,height=600)



        title_lbl=Label(bg_img,text="ATTENDANCE  MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1280,height=40)



        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=50,y=60,width=1180,height=500)


        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=10,width=560,height=470)


        #labels and entry
        #ID
        attendanceId_label=Label(Left_frame,text="Attendance Id:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendanceId_entry=ttk.Entry(Left_frame,width=25,textvariable=self.var_id,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)


        #Roll
        roll_label=Label(Left_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        roll_entry=ttk.Entry(Left_frame,width=25,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=1,padx=5,pady=10,sticky=W)



        #Name
        name_label=Label(Left_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        name_entry=ttk.Entry(Left_frame,width=25,textvariable=self.var_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)



        #Dept
        dept_label=Label(Left_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dept_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        dept_entry=ttk.Entry(Left_frame,width=25,textvariable=self.var_dept,font=("times new roman",13,"bold"))
        dept_entry.grid(row=3,column=1,padx=5,pady=10,sticky=W)



        #Date
        date_label=Label(Left_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        date_entry=ttk.Entry(Left_frame,width=25,textvariable=self.var_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=4,column=1,padx=5,pady=10,sticky=W)



        #Time
        time_label=Label(Left_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        time_entry=ttk.Entry(Left_frame,width=25,textvariable=self.var_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=5,column=1,padx=5,pady=10,sticky=W)



        #attendance
        attendance_label=Label(Left_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        self.attendance_combo=ttk.Combobox(Left_frame,textvariable=self.var_attendance,font=("times new roman",10,"bold"),state="readonly",width=30)
        self.attendance_combo["values"]=("Status","Present","Absent")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=6,column=1,padx=5,pady=10,sticky=W)



        #buttons
        #Buttons Frame

        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=330,width=537,height=102)



        imp_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=20,cursor="hand1",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        imp_btn.grid(row=0,column=0,padx=8,pady=4)

        expo_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=20,cursor="hand1",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        expo_btn.grid(row=0,column=1,padx=8,pady=4)

        help_btn=Button(btn_frame,text="Help",command=self.helpdesk,width=20,cursor="hand1",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        help_btn.grid(row=1,column=1,padx=8,pady=4)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,cursor="hand1",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=1,column=0,padx=8,pady=4)



        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=595,y=10,width=560,height=470) 


        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=10,width=535,height=424)


        #scroll-bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","dept","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("roll",text="Roll No.")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dept",text="Department")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dept",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



    #fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    def importCsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)



    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data exported successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)




    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dept.set(rows[3])
        self.var_date.set(rows[4])
        self.var_time.set(rows[5])
        self.var_attendance.set(rows[6])



    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_attendance.set("")




    def helpdesk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)









if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()    