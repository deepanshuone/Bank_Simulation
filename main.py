from tkinter import Tk,Label,Frame,Button,Entry,messagebox,simpledialog
import time
import TableCreater
from datetime import datetime
import EmailHandler
import generator
import sqlite3
TableCreater.create()
def update_time():
    curdate=time.strftime("%d-%b-%Y ⏰%r")
    date.configure(text=curdate)
    date.after(1000,update_time)




def forgot_screen():
    def back():
        frm.destroy()
        existuser_screen()
    
    def update_otp(user_otp,otp,acn):
        
        for i in range(3,0,-1):
                # i=3
            if(user_otp==otp):
                user_pass=simpledialog.askstring("Update Password","Enter New Password")
                conobj=sqlite3.connect(database='mybank.sqlite')
                curobj=conobj.cursor()
                curobj.execute('update accounts set pass=? where acn=?',(user_pass,acn))

                conobj.commit()
                conobj.close()
                break
            else:
                user_otp=simpledialog.askinteger("Wrong OTP",f"Only {i} chance left")
        if(user_otp!=otp):
            otp_btn.configure(text='Resend OTP')

        

    def send_otp():
    
        otp=generator.otp_generator()
        acn=e_acn.get()
        adhar=e_adhar.get()
        
        conobj=sqlite3.connect(database='mybank.sqlite')
        curobj=conobj.cursor()
        query='select name,pass,email from accounts where acn=? and adhar=?'
        curobj.execute(query,(acn,adhar))
        tup=curobj.fetchone()
        conobj.commit()
        conobj.close()
        print(tup)
        name=tup[0]
        email=tup[2]
        pwd=tup[1]
        
        if tup==None:
            messagebox.showerror("Forget Password ","Record Not Found")
        else:
            EmailHandler.otp_email(email,name,otp)
            user_otp=simpledialog.askinteger("Required For Forget Pwd","Enter OTP")
            update_otp(user_otp,otp,acn)



            
        
        

    frm=Frame(root,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.7)

    back_btn=Button(frm,text='Back',bg='powder blue',font=('arial',20,'bold'),bd=5,command=back)
    back_btn.place(relx=0,rely=0)
 
    lbl_acn=Label(frm,text='ACN',width=7,font=('arial',20,'bold'),bg='purple',fg='white')
    lbl_acn.place(relx=.3,rely=.2)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.2)
    e_acn.focus()

    lbl_adhar=Label(frm,text='Adhar',width=7,font=('arial',20,'bold'),bg='purple',fg='white')
    lbl_adhar.place(relx=.3,rely=.3)

    e_adhar=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_adhar.place(relx=.4,rely=.3)

    otp_btn=Button(frm,text='Send OTP',width=8,bg='powder blue',font=('arial',20,'bold'),bd=5,command=send_otp)
    otp_btn.place(relx=.35,rely=.5)

    reset_btn=Button(frm,text='Reset',width=8,bg='powder blue',font=('arial',20,'bold'),bd=5)
    reset_btn.place(relx=.5,rely=.5)

def welcome_screen(acn1):
    def logout():
        frm.destroy()
        main_screen()

    def check_screen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.27,rely=.1,relwidth=.6,relheight=.66)


        title_lbl=Label(ifrm,text="This is Check Details Screen",
                        font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("Select * from accounts where acn=?",(acn1,))
        tup=curobj.fetchone()
        lbl_Acon=Label(ifrm,text="Acount No",font=('arial',20,'bold'))
        lbl_Acon.place(relx=.01,rely=0.1)
        lbl_Acn=Label(ifrm,text=acn1,font=('arial',20,'bold'))
        lbl_Acn.place(relx=.3,rely=0.1)
        lbl_Name=Label(ifrm,text="Name",font=('arial',20,'bold'))
        lbl_Name.place(relx=.02,rely=0.25)
        lbl_Name1=Label(ifrm,text=tup[1],font=('arial',20,'bold'))
        lbl_Name1.place(relx=.3,rely=0.25)
        lbl_mob=Label(ifrm,text="Mobile No",font=('arial',20,'bold'))
        lbl_mob.place(relx=.02,rely=0.4)
        lbl_mob1=Label(ifrm,text=tup[3],font=('arial',20,'bold'))
        lbl_mob1.place(relx=.3,rely=0.4)
        lbl_email=Label(ifrm,text="Email",font=('arial',20,'bold'))
        lbl_email.place(relx=.02,rely=0.55)
        lbl_email1=Label(ifrm,text=tup[4],font=('arial',20,'bold'))
        lbl_email1.place(relx=.3,rely=0.55)
        lbl_adhar=Label(ifrm,text="Adhar Address",font=('arial',20,'bold'))
        lbl_adhar.place(relx=.02,rely=0.7)
        lbl_adhar1=Label(ifrm,text=tup[5],font=('arial',20,'bold'))
        lbl_adhar1.place(relx=.3,rely=0.7)
        lbl_bal=Label(ifrm,text="Balance",font=('arial',20,'bold'))
        lbl_bal.place(relx=.02,rely=0.85)
        lbl_bal1=Label(ifrm,text=tup[6],font=('arial',20,'bold'))
        lbl_bal1.place(relx=.3,rely=0.85)
        conobj.commit()
        conobj.close()


        

    def update_screen():

        def update_db():
            acn=e_Acn.get()
            name=e_Name1.get()
            mobile=e_mob1.get()
            email=e_email1.get()
            adhar=e_adhar1.get()
            pwd=e_pas1.get()
            conobj=sqlite3.connect(database="mybank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("update accounts set name=?,mob=?,email=?,adhar=?,pass=? where acn=?",(name,mobile,email,adhar,pwd,acn))
            conobj.commit()
            conobj.close()
            messagebox.Message("Data Upload Successfully")
            welcome_screen(acn1)
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.27,rely=.1,relwidth=.6,relheight=.66)

        title_lbl=Label(ifrm,text="This is Update Details Screen",
                        font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        print(acn1)
        curobj.execute("Select * from accounts where acn=?",(acn1,))
        tup=curobj.fetchone()
        lbl_Acon=Label(ifrm,text="Account No",font=('arial',20,'bold'))
        lbl_Acon.place(relx=.01,rely=0.1)
        e_Acn=Entry(ifrm,font=('arial',20,'bold'))
        e_Acn.place(relx=.3,rely=0.1)
        e_Acn.insert(0,tup[0])

        lbl_Name=Label(ifrm,text="Name",font=('arial',20,'bold'))
        lbl_Name.place(relx=.02,rely=0.25)
        e_Name1=Entry(ifrm,font=('arial',20,'bold'))
        e_Name1.place(relx=.3,rely=0.25)
        e_Name1.insert(0,tup[1])
        lbl_mob=Label(ifrm,text="Mobile No",font=('arial',20,'bold'))
        lbl_mob.place(relx=.02,rely=0.4)
        e_mob1=Entry(ifrm,font=('arial',20,'bold'))
        e_mob1.place(relx=.3,rely=0.4)
        e_mob1.insert(0,tup[3])

        lbl_email=Label(ifrm,text="Email",font=('arial',20,'bold'))
        lbl_email.place(relx=.02,rely=0.55)
        e_email1=Entry(ifrm,font=('arial',20,'bold'))
        e_email1.place(relx=.3,rely=0.55)
        e_email1.insert(0,tup[4])

        lbl_adhar=Label(ifrm,text="Adhar Address",font=('arial',20,'bold'))
        lbl_adhar.place(relx=.02,rely=0.7)
        e_adhar1=Entry(ifrm,font=('arial',20,'bold'))
        e_adhar1.place(relx=.3,rely=0.7)      
        e_adhar1.insert(0,tup[5])

        lbl_pas=Label(ifrm,text="Password",font=('arial',20,'bold'))
        lbl_pas.place(relx=.02,rely=0.85)
        e_pas1=Entry(ifrm,font=('arial',20,'bold'))
        e_pas1.place(relx=.3,rely=0.85)
        e_pas1.insert(0,tup[2])



        submit_btn=Button(frm,text='Submit',width=8,bg='powder blue',font=('arial',20,'bold'),bd=5,command=update_db)
        submit_btn.place(relx=.7,rely=.5)
    
    def deposit_screen():
        def deposite_db():
            bal1=float(e_bal1.get())
            acn=e_Acn.get()
            
            conobj=sqlite3.connect(database="mybank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select bal from accounts where acn=?",(acn,))
            bal=curobj.fetchone()
            curobj.execute("update accounts set bal=? where acn=?",(bal[0]+bal1,acn))

            conobj.commit()
            conobj.close()

        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.27,rely=.1,relwidth=.6,relheight=.66)

        title_lbl=Label(ifrm,text="This is Deposit Amount Screen",
                        font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()

        lbl_Acon=Label(ifrm,text="Account No",font=('arial',20,'bold'))
        lbl_Acon.place(relx=.01,rely=0.1)
        e_Acn=Entry(ifrm,font=('arial',20,'bold'))
        e_Acn.place(relx=.4,rely=0.1)

        lbl_bal1=Label(ifrm,text="Deposite Amount",font=('arial',20,'bold'))
        lbl_bal1.place(relx=.01,rely=0.25)
        e_bal1=Entry(ifrm,font=('arial',20,'bold'))
        e_bal1.place(relx=.4,rely=0.25)
        submit_btn=Button(frm,text='Submit',width=8,bg='powder blue',font=('arial',20,'bold'),bd=5,command=deposite_db)
        submit_btn.place(relx=.7,rely=.5)
    
    def withdraw_screen():
        def withdraw_db():
            bal1=float(e_bal1.get())
            acn=e_Acn.get()
            
            conobj=sqlite3.connect(database="mybank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select bal from accounts where acn=?",(acn,))
            bal=curobj.fetchone()
            if(bal[0]>=bal1):
                curobj.execute("update accounts set bal=? where acn=?",(bal[0]-bal1,acn))
            else:
                messagebox.showerror("Error", f"Your account balance is insufficient. Bal is{bal[0]}")
            conobj.commit()
            conobj.close()
        
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.27,rely=.1,relwidth=.6,relheight=.66)

        title_lbl=Label(ifrm,text="This is Withdraw Amount Screen",
                        font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()

        lbl_Acon=Label(ifrm,text="Account No",font=('arial',20,'bold'))
        lbl_Acon.place(relx=.01,rely=0.1)
        e_Acn=Entry(ifrm,font=('arial',20,'bold'))
        e_Acn.place(relx=.4,rely=0.1)

        lbl_bal1=Label(ifrm,text="Withdraw Amount",font=('arial',20,'bold'))
        lbl_bal1.place(relx=.01,rely=0.25)
        e_bal1=Entry(ifrm,font=('arial',20,'bold'))
        e_bal1.place(relx=.4,rely=0.25)
        submit_btn=Button(frm,text='Submit',width=8,bg='powder blue',font=('arial',20,'bold'),bd=5,command=withdraw_db)
        submit_btn.place(relx=.7,rely=.5)
    
    def transfer_screen():
        def transfer_db():
            bal1=float(e_bal1.get())
            acn=e_Acn.get()
            
            conobj=sqlite3.connect(database="mybank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select bal from accounts where acn=?",(acn1,))
            user_bal=curobj.fetchone()
            if (user_bal[0]>=bal1):
                print(acn)
                curobj.execute("select bal from accounts where acn=?",(acn,))
                bal=curobj.fetchone()
                curobj.execute("update accounts set bal=? where acn=?",(bal[0]+bal1,acn))
                curobj.execute("update accounts set bal=? where acn=?",(user_bal[0]-bal1,acn1))
                messagebox.showinfo("Payment Status", f"Transfer {bal1} from your Account")
            else :
                messagebox.Message(f"No Sufficient Balance Available Your Bal is {user_bal[0]}")
            
            conobj.commit()
            conobj.close()
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.27,rely=.1,relwidth=.6,relheight=.66)

        title_lbl=Label(ifrm,text="This is Transfer Amount Screen",
                        font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        
        lbl_Acon=Label(ifrm,text="Account No",font=('arial',20,'bold'))
        lbl_Acon.place(relx=.01,rely=0.1)
        e_Acn=Entry(ifrm,font=('arial',20,'bold'))
        e_Acn.place(relx=.4,rely=0.1)

        lbl_bal1=Label(ifrm,text="Transfer Amount",font=('arial',20,'bold'))
        lbl_bal1.place(relx=.01,rely=0.25)
        e_bal1=Entry(ifrm,font=('arial',20,'bold'))
        e_bal1.place(relx=.4,rely=0.25)
        submit_btn=Button(frm,text='Submit',width=8,bg='powder blue',font=('arial',20,'bold'),bd=5,command=transfer_db)
        submit_btn.place(relx=.7,rely=.5)


    

    frm=Frame(root,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.11,relwidth=1,relheight=.8)
    conobj=sqlite3.connect(database="mybank.sqlite")
    curobj=conobj.cursor()
    curobj.execute("select name from accounts where acn=?",(acn1,))
    tup=curobj.fetchone()
    logout_btn=Button(frm,text='Logout',bg='powder blue',font=('arial',20,'bold'),bd=5,command=logout)
    logout_btn.place(relx=.9,rely=0.1)

    lbl_wel=Label(frm,text=f'Welcome, {tup[0]}',font=('arial',20,'bold'),bg='purple',fg='white')
    lbl_wel.place(relx=.17,rely=0.01)

    check_btn=Button(frm,text='Check Details',width=15,bg='powder blue',font=('arial',20,'bold'),bd=5,command=check_screen)
    check_btn.place(relx=.001,rely=.25)

    update_btn=Button(frm,text='Update Details',width=15,bg='powder blue',font=('arial',20,'bold'),bd=5,command=update_screen)
    update_btn.place(relx=.001,rely=.4)

    deposit_btn=Button(frm,text='Deposit Amount',width=15,bg='green',fg='white',font=('arial',20,'bold'),bd=5,command=deposit_screen)
    deposit_btn.place(relx=.001,rely=.55)

    withdraw_btn=Button(frm,text='Withdraw Amount',width=15,bg='red',fg='white',font=('arial',20,'bold'),bd=5,command=withdraw_screen)
    withdraw_btn.place(relx=.001,rely=.7)

    transfer_btn=Button(frm,text='Transfer Amount',width=15,bg='red',fg='white',font=('arial',20,'bold'),bd=5,command=transfer_screen)
    transfer_btn.place(relx=.001,rely=.85)
    conobj.close()

def existuser_screen():
    def back():
        frm.destroy()
        main_screen()

    def fp_click():
        frm.destroy()
        forgot_screen()

    def submit_click():
        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        acn1=e_acn.get()
        pwd=e_pass.get()
        curobj.execute("select * from accounts where acn=? and pass=?",(acn1,pwd))
        tup=curobj.fetchone()
        if(tup==None):
            messagebox.showerror("Login","Invalid Credentials")
        else:
                frm.destroy()
                welcome_screen(acn1)
        conobj.commit()
        conobj.close()


    frm=Frame(root,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.86)

    back_btn=Button(frm,text='Back',bg='powder blue',font=('arial',20,'bold'),bd=5,command=back)
    back_btn.place(relx=0,rely=0)

    lbl_acn=Label(frm,text='ACN',width=7,font=('arial',20,'bold'),bg='purple',fg='white')
    lbl_acn.place(relx=.3,rely=.2)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.2)
    e_acn.focus()

    lbl_pass=Label(frm,text='Pass',width=7,font=('arial',20,'bold'),bg='purple',fg='white')
    lbl_pass.place(relx=.3,rely=.3)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.4,rely=.3)

    submit_btn=Button(frm,text='Submit',width=6,bg='powder blue',font=('arial',20,'bold'),bd=5,command=submit_click)
    submit_btn.place(relx=.4,rely=.5)

    reset_btn=Button(frm,text='Reset',width=6,bg='powder blue',font=('arial',20,'bold'),bd=5)
    reset_btn.place(relx=.5,rely=.5)

    fp_btn=Button(frm,text='Forgot Password',width=18,bg='powder blue',font=('arial',20,'bold'),bd=5,command=fp_click)
    fp_btn.place(relx=.38,rely=.6)


def newuser_screen():
    def back():
        frm.destroy()
        main_screen()
    def createacn_db():
        name=e_name.get()
        email=e_email.get()
        mob=e_mob.get()
        adhar=e_adhar.get()
        bal=0
        opendate=datetime.now()
        pwd=generator.generate_pass()
        query='''insert into accounts values(?,?,?,?,?,?,?,?)'''
        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        curobj.execute(query,(None,name,pwd,mob,email,adhar,bal,opendate))
        conobj.commit()
        conobj.close()
                
        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        query='''select max(acn) from accounts'''
        curobj.execute(query)
        tup=curobj.fetchone()
        EmailHandler.send_credentials(email,name,tup[0],pwd)
        messagebox.showinfo('Account Creation','Your account is opened ')



    

    frm=Frame(root,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.75)

    back_btn=Button(frm,text='Back',bg='powder blue',font=('arial',20,'bold'),bd=5,command=back)
    back_btn.place(relx=0,rely=0)

    lbl_name=Label(frm,text='👨‍💼Name',width=7,font=('arial',20,'bold'),bg='purple',fg='white')
    lbl_name.place(relx=.1,rely=.2)

    e_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.place(relx=.2,rely=.2)
    e_name.focus()

    lbl_email=Label(frm,text='Email',width=7,font=('arial',20,'bold'),bg='purple',fg='white')
    lbl_email.place(relx=.1,rely=.3)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.2,rely=.3)


    lbl_mob=Label(frm,text='📱Mob',width=7,font=('arial',20,'bold'),bg='purple',fg='white')
    lbl_mob.place(relx=.5,rely=.2)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.6,rely=.2)

    lbl_adhar=Label(frm,text='Adhar',width=7,font=('arial',20,'bold'),bg='purple',fg='white')
    lbl_adhar.place(relx=.5,rely=.3)

    e_adhar=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_adhar.place(relx=.6,rely=.3)

    submit_btn=Button(frm,text='Submit',width=8,bg='powder blue',font=('arial',20,'bold'),bd=5,command=createacn_db)
    submit_btn.place(relx=.35,rely=.5)

    reset_btn=Button(frm,text='Reset',width=8,bg='powder blue',font=('arial',20,'bold'),bd=5)
    reset_btn.place(relx=.5,rely=.5)


def main_screen():
    
    def newuser_click():
        frm.destroy()
        newuser_screen()
    
    def existuser_click():
        frm.destroy()
        existuser_screen()

    frm=Frame(root,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.13,relwidth=1,relheight=.74)

    newuser_btn=Button(frm,text='New User\nCreate Account',
                       font=('arial',20,'bold'),
                       fg='black',
                       bg='powder blue',
                       bd=5,
                       width=15,
                       activebackground='purple',
                       activeforeground='white',
                       command=newuser_click)
    
    newuser_btn.place(relx=.27,rely=.3)

    existuser_btn=Button(frm,text='Existing User\nSign In',
                       font=('arial',20,'bold'),
                       fg='black',
                       bg='powder blue',
                       bd=5,
                       width=15,
                       activebackground='purple',
                       activeforeground='white',
                       command=existuser_click)
    existuser_btn.place(relx=.5,rely=.3)

root=Tk()   
root.state('zoomed') 
root.resizable(width=False,height=False)
root.configure(bg='powder blue')

title=Label(root,text="Banking Simulation",
            font=('arial',50,'bold','underline'),bg='powder blue')
title.pack()

curdate=time.strftime("%d-%b-%Y ⏰%r")
date=Label(root,text=curdate,
           font=('arial',20,'bold'),bg='powder blue',fg='blue')
date.pack(pady=15)
update_time()

footer=Label(root,text="Developed by:sonu kumar \n📱 9999999999",
            font=('arial',20,'bold'),bg='powder blue')
footer.pack(side='bottom')

main_screen()

root.mainloop() #to make window visible
