from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    PasswordEntry.delete(0,END)
    ConfirmEntry.delete(0,END)
    check.set(0)

    
def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or PasswordEntry.get()=='' or ConfirmEntry.get()=='':
        messagebox.showerror('Error','all fields are requiblack')
    elif PasswordEntry.get()!=ConfirmEntry.get():
        messagebox.showerror('Error','Password Mismatched')
    elif check.get()==0:
         messagebox.showerror('Error','Please accept terms & conditions')
    else:
        try:
            
            con=pymysql.connect(host='localhost',user='root',password='Realtime123*')
            mycursor=con.cursor()

        except:
            messagebox.showerror('Error','database connectivity issue,please try again')
            return
                                
            
        try:
            

            query='create database userdata1'
            mycursor.execute(query)
            query='use userdata1'
            mycursor.execute(query)
            query='create table data1(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata1')

            query='select * from data1 where username=%s'
            mycursor.execute(query,(usernameEntry.get()))


            row=mycursor.fetchone()
            if row !=None:
                messagebox.showerror('Error','Username already Exists')
            else:
                
                
                query='insert into data1(email,username,password) values(%s,%s,%s)'
                mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),PasswordEntry.get()))
                con.commit()

                con.close()
                messagebox.showinfo('Success','Registration is successfull')
                clear()
                signup_window.destroy()
                import login
       

def login_page():
    signup_window.destroy()
    import login

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False, False)





background=ImageTk.PhotoImage(file='images/bg.jpg')




bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='black')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='black')
emailLabel.grid(row=1,column=0,sticky='w')


emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10, 'bold'), bg='black', fg='white')
emailEntry.grid(row=2,column=0,sticky='w')

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='black')
usernameLabel.grid(row=3,column=0,sticky='w')

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10, 'bold'), bg='black', fg='white')
usernameEntry.grid(row=4,column=0,sticky='w')

PasswordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='black')
PasswordLabel.grid(row=5,column=0,sticky='w')

PasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10, 'bold'), bg='black', fg='white')
PasswordEntry.grid(row=6,column=0,sticky='w')



ConfirmLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='black')
ConfirmLabel.grid(row=7,column=0,sticky='w')

ConfirmEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10, 'bold'), bg='black', fg='white')
ConfirmEntry.grid(row=8,column=0,sticky='w')

check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='black',activebackground='white',activeforeground='black',cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,sticky='w')


signupButton=Button(frame,text='Sign Up',font=('Open Sans', 16, 'bold'), bd=0,bg='black',fg='white',activebackground='black',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,sticky='w',pady=10)



alreadyaccount=Label(frame,text="Don't have an Account? ",font=('Open Sans', 9, 'bold'),bg='white',fg='black')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10,columnspan=2)


loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.grid(row=11,column=1,sticky='w')


signup_window.mainloop()
