from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_Attendance


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1280x700+0+0")
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



        frame=Frame(self.root,bg="black")
        frame.place(x=480,y=170,width=330,height=450)


        
        img4=Image.open(r"C:\Users\Mohit Kumar\OneDrive\Desktop\Face_Recognition_Attendance\images\user1.png")
        img4=img4.resize((100,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(image=self.photoimg4,bg="white",borderwidth=0)
        f_lbl.place(x=600,y=185,width=90,height=90)


        get_str=Label(frame,text="Admin Login",font=("times new roman",25,"bold"),bg="black",fg="red")
        get_str.place(x=65,y=110)



        #labels
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="white")
        username_lbl.place(x=118,y=160)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=20,y=185,width=292)


        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        password_lbl.place(x=118,y=230)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=20,y=255,width=292)

        
        #login button
        loginbtn=Button(frame,text="Login",cursor="hand1",command=self.login,font=("times new roman",15,"bold"),bg="red",fg="white",bd=2,relief=RIDGE,activeforeground="white",activebackground="red")
        loginbtn.place(x=105,y=300,width=120,height=30)



        #register button
        registerbtn=Button(frame,text="Register New User",cursor="hand1",command=self.register_window,font=("times new roman",15,"bold"),bg="black",fg="white",borderwidth=0,activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=160)


        #forgot password button
        forgotpassbtn=Button(frame,text="Forgot Password",cursor="hand1",command=self.forgot_password_window,font=("times new roman",15,"bold"),bg="black",fg="white",borderwidth=0,activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=13,y=390,width=160)




    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)




    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="mohit" and self.txtpass.get()=="bittu":
            messagebox.showinfo("Success","Welcome to Face Recognition System")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                    ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_Attendance(self.new_window)
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()


    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select a security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="mydata")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password has been reset successfully",parent=self.root2)
                self.root2.destroy()






    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the registered email")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@1",database="mydata")
            my_cursor=conn.cursor()
            quer=("select * from register where email=%s")
            valu=(self.txtuser.get(),)
            my_cursor.execute(quer,valu)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birthplace","Your Rolemodel","Your petname")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=250)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)



                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)




                btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="darkblue")
                btn.place(x=100,y=290)






            

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1280x700+0+0")



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


        b2=Button(frame,text="Login Now",cursor="hand1",command=self.return_login,font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=2,relief=RIDGE,activeforeground="white",activebackground="darkblue")
        b2.place(x=440,y=470,width=150,height=50)




    #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to the terms and conditions",parent=self.root)
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
            messagebox.showinfo("Success","Registered successfully",parent=self.root)



    def return_login(self):
        self.root.destroy()








if __name__ == "__main__":
    main()
