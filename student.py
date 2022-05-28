from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar() 
        self.var_gender=StringVar()
        self.var_teacher=StringVar()
        



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



        #background image
        img3=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\website-background-image-size-psd-vector-photo.jpg")
        img3=img3.resize((1280,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1280,height=600)



        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=40)



        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=50,y=60,width=1180,height=500)


        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=10,width=560,height=470)


        #Course details
        Course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Details", font=("times new roman",12,"bold"))
        Course_frame.place(x=10,y=3,width=535,height=120)

        #Department
        dep_label=Label(Course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5,sticky=W)

        dep_combo=ttk.Combobox(Course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","CSE","IT","ECE","EEE","Civil","Mech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)



        #Course
        course_label=Label(Course_frame,text="     Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(Course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","B.Tech","M.Tech","I.Msc","Phd")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)



        #Year
        year_label=Label(Course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        year_combo=ttk.Combobox(Course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)



        #Semester
        sem_label=Label(Course_frame,text="     Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=5,sticky=W)

        sem_combo=ttk.Combobox(Course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly",width=17)
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #Student Information
        Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information", font=("times new roman",12,"bold"))
        Student_frame.place(x=10,y=136,width=535,height=305)

        
        #Student Id
        studentId_label=Label(Student_frame,text="Student Id",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,sticky=W)

        studentId_entry=ttk.Entry(Student_frame,textvariable=self.var_id,width=15,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,sticky=W)



        #Student Name
        studentname_label=Label(Student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        studentname_entry=ttk.Entry(Student_frame,textvariable=self.var_name,width=15,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)



        #Roll Number
        roll_label=Label(Student_frame,text="Roll Number",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=5,sticky=W)

        roll_entry=ttk.Entry(Student_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=1,padx=5,sticky=W)



        #DOB
        dob_label=Label(Student_frame,text="D.O.B.",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=5,sticky=W)

        dob_entry=ttk.Entry(Student_frame,textvariable=self.var_dob,width=15,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=3,padx=5,sticky=W)



        #Phone Number
        phone_label=Label(Student_frame,text="Phone Number",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=2,column=0,padx=5,sticky=W)

        phone_entry=ttk.Entry(Student_frame,textvariable=self.var_phone,width=15,font=("times new roman",12,"bold"))
        phone_entry.grid(row=2,column=1,padx=5,sticky=W)



        #Email
        email_label=Label(Student_frame,text="E-mail",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        email_entry=ttk.Entry(Student_frame,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=3,padx=5,sticky=W)



        #Gender
        gender_label=Label(Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=3,column=0,padx=5,sticky=W)

        gender_combo=ttk.Combobox(Student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly",width=15)
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=5,sticky=W)



        #Teacher Name
        teacher_label=Label(Student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=3,column=2,padx=5,sticky=W)

        teacher_entry=ttk.Entry(Student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=3,column=3,padx=5,sticky=W)



        #Radio Buttons
        self.var_radio1=StringVar()
        radio_btn_1=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_btn_1.grid(row=5,column=0,padx=5,pady=5)

        radio_btn_2=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_btn_2.grid(row=5,column=1,pady=5)


        #Buttons Frame

        btn_frame=Frame(Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=180,width=521,height=92)



        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,cursor="hand1",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=6)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,cursor="hand1",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=6)

        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=17,cursor="hand1",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2,padx=5,pady=6)

        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=17,cursor="hand1",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=1,column=0,padx=5,pady=5)

        takepic_btn=Button(btn_frame,command=self.generate_dataset,text="Take a Photo Sample",width=17,cursor="hand1",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        takepic_btn.grid(row=1,column=1,padx=5,pady=5)

        updatepic_btn=Button(btn_frame,text="Update Photo Sample",width=17,cursor="hand1",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        updatepic_btn.grid(row=1,column=2,padx=5,pady=5)
        


        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=595,y=10,width=560,height=470) 



        # =======Search System=======

        


        #Table Frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=10,width=535,height=420)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","roll","dob","phone","email","gender","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("dob",text="D.O.B.")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=119)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #Function Declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_gender.get()=="Select Gender"or self.var_teacher.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
             try: 
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student Details have been added successfully",parent=self.root)
             except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_email.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_teacher.set(data[11]),
        self.var_radio1.set(data[12])



    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_gender.get()=="Select Gender"or self.var_teacher.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the Student Details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,roll=%s,dob=%s,phone=%s,email=%s,gender=%s,teacher=%s,PhotoSample=%s where student_id=%s",(  
                                                                                                                                                                                                    self.var_dep.get(),                                                                                                        
                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                    self.var_radio1.get(),  
                                                                                                                                                                                                    self.var_id.get()
                                                                                                                                                                                                ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted Student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



        
    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_gender.set("Select Gender")
        self.var_teacher.set("")
        self.var_radio1.set("")




    #Generate data set or take Photo Samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_gender.get()=="Select Gender"or self.var_teacher.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                idd=0
                for x in myresult:
                    idd+=1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,roll=%s,dob=%s,phone=%s,email=%s,gender=%s,teacher=%s,PhotoSample=%s where student_id=%s",(  
                                                                                                                                                                                                    self.var_dep.get(),                                                                                                        
                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                    self.var_radio1.get(),  
                                                                                                                                                                                                    self.var_id.get()==idd+1
                                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on frontal face from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(idd)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data Sets generated successfully")

            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)






if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()    