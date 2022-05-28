from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
# from mysql import mysql.connector 



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1280x700+0+0")
        self.root.wm_iconbitmap("face.ico")



        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\website-background-image-size-psd-vector-photo.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        frame=Frame(self.root,bg="white")
        frame.place(x=300,y=80,width=700,height=550)



        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)


        #labels and entries

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=90)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=120,width=250)




        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=390,y=90)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=390,y=120,width=250)




        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)





        email=Label(frame,text="Email Id",font=("times new roman",15,"bold"),bg="white")
        email.place(x=390,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=390,y=200,width=250)



        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=250)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birthplace","Your Rolemodel","Your petname")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=280,width=250)




        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=390,y=250)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=390,y=280,width=250)




        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=330)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=360,width=250)




        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=390,y=330)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=390,y=360,width=250)


        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to the terms and conditions",font=("times new roman",11,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=415)



        b1=Button(frame,text="Register",cursor="hand1",command=self.register_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=2,relief=RIDGE,activeforeground="white",activebackground="darkblue")
        b1.place(x=96,y=470,width=150,height=50)


        b2=Button(frame,text="Login Now",cursor="hand1",font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=2,relief=RIDGE,activeforeground="white",activebackground="darkblue")
        b2.place(x=440,y=470,width=150,height=50)




    #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to the terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already registered")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully")





if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()