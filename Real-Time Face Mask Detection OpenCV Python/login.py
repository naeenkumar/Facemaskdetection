from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
import shutil
import sys
import tkinter as tk
from PIL import ImageTk
import pymysql



# Functionality part

def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=window)
        elif newpass_entry.get() !=confirmpass_entry.get():
            messagebox.showerror('Error','password and confirm password are not matching',parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='Realtime123*',database='userdata1')
            mycursor=con.cursor()
            query='select * from data1 where username=%s '
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect username',parent=window)
            else:
                query='Update data1 set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset,Please login with new password',parent=window)
                window.destroy()
                
            
            
    window=Toplevel(login_window)
    window.title('Change Password')
    
    bgPic = ImageTk.PhotoImage(file='images/background.jpg')
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid(row=0,column=0)

    heading = Label(window, text='RESET PASSWORD', font=('arial', 18, 'bold'), bg='white', fg='black')
    heading.place(x=480, y=60)

    userLabel = Label(window, text='Username', font=('arial', 12, 'bold'), bg='white', fg='black')
    userLabel.place(x=470, y=130)

    user_entry = Entry(window, width=25, font=('arial',11,'bold'),bd=0, fg='black')
    user_entry.place(x=470, y=160)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=180)

    passwordLabel = Label(window, text='New Password', font=('arial', 12, 'bold'), bg='white', fg='black')
    passwordLabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25 , font=('arial', 11, 'bold'), bd=0, fg='black')
    newpass_entry.place(x=470, y=240)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=260)

    confirmpassLabel = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), bg='white', fg='black')
    confirmpassLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='black')
    confirmpass_entry.place(x=470, y=320)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=340)

    
    submitButton=Button(window,text='Submit',font=('Open Sans', 16, 'bold'), bd=0,bg='green',fg='white',activebackground='green',activeforeground='white',width=19, command=change_password)
    submitButton.place(x=470,y=390)
 
    
    window.mainloop()



def login_user():
     if usernameEntry.get()=='' or passwordEntry.get()=='':
         messagebox.showerror('Error','All fields are required')
     else:
          
         try:
             
             con=pymysql.connect(host='localhost',user='root',password='Realtime123*')
             mycursor=con.cursor()
        
             
             query='use userdata1'
        
            
             mycursor.execute(query)
             query='select * from data1 where username=%s and password=%s'
             mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
             row=mycursor.fetchone()
             if row==None:
                 messagebox.showerror('Error','Invalid Username or password')
             else:
                messagebox.showinfo('done with login',command=process())
             con.close()
             
             
             

         except pymysql.Error as e:
             
             messagebox.showerror('Error','connection is not established try again')
def process():
    login_window.destroy()
    import main           
 
        
def signup_page():
    login_window.destroy()
    import Signup

def hide():
    openeye.config(file='images/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='images/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get() == 'username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'password':
        passwordEntry.delete(0, END)



# GUI part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0, 0)
login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='images/bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('MICROSOFT Yahei UI Light', 23, 'bold'), bg='white', fg='red')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='red')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=250, height=2, bg='red')
frame1.place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='red')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'password')
passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width=250, height=2, bg='red')
frame2.place(x=580, y=282)

openeye = PhotoImage(file='images/closeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='forgot password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('Microsoft Yahei UI Light', 9, 'bold'), fg='red', activeforeground='red', command=forget_pass)
forgetButton.place(x=715, y=295)

loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='red',
                     activeforeground='white', activebackground='red', cursor='hand2', bd=0, width=19)
loginButton.place(x=578, y=350)
loginButton.config(command=login_user)

orLabel = Label(login_window, text='------------------- OR ------------', font=('Open Sans', 16), fg='red', bg='white')
orLabel.place(x=583, y=400)

facebook_logo = PhotoImage(file='images/facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640, y=440)

google_logo = PhotoImage(file='images/google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file='images/twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740, y=440)

signupLabel = Label(login_window, text='Dont have an account?', font=('Open Sans', 9, 'bold'), fg='red', bg='white')
signupLabel.place(x=590, y=500)

newaccountButton = Button(login_window, text='create new one', font=('Open Sans', 9, 'bold'), fg='red', bg='white',
                          activeforeground='blue', activebackground='red', cursor='hand2', bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)

login_window.mainloop()

