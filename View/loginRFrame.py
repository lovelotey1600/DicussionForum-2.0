import sys
sys.path.append("..")
import tkinter as tk
import tkinter.ttk as ttk
from View.registrationFrame import *
from View.homeFrame import *
from Controller.signupIN import *
from tkinter import messagebox

class loginRFrame:
    def register(self):
        if self.rID.get()=="":
           messagebox.showinfo("Registration"," You need to enter some user ID")   
        else:
            u=self.rID.get()
            u="@"+u
            u=u.strip()
            self.rgLFrame.destroy()
            m=registrationFrame(self.f,u)
    
    def toggleLoginUI(self):
        if self.lID.get=="" and self.lpass.get()=="":
            messagebox.showinfo("Log in","You need to enter some user id and password.")
        else:
            uid=self.lID.get()
            uid="@"+uid
            pd=self.lpass.get()
            uid=uid.strip()
            pd=pd.strip()
            l=login
            chk = l.usrlogin(l,uid,pd)
            if chk==1:
                h=homeFrame(self.f)

                

    def __init__(self, top=None):
        font10 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.f=top
        self.rgLFrame = ttk.Frame(top)
        self.rgLFrame.place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.501)
        self.rgLFrame.configure(relief='groove')
        self.rgLFrame.configure(borderwidth="2")
        self.rgLFrame.configure(relief="groove")
        self.rgLFrame.configure(width=385)

        self.TSeparator1 = ttk.Separator(self.rgLFrame)
        self.TSeparator1.place(relx=0.499, rely=0.0, relheight=1.0)
        self.TSeparator1.configure(orient="vertical")

        self.registerL = ttk.Label(self.rgLFrame)
        self.registerL.place(relx=0.15, rely=0.167, height=40, width=80)
        self.registerL.configure(foreground="#000000")
        self.registerL.configure(font=font10)
        self.registerL.configure(relief="flat")
        self.registerL.configure(text='''Register''')
        self.registerL.configure(width=80)

        self.loginL = ttk.Label(self.rgLFrame)
        self.loginL.place(relx=0.686, rely=0.167, height=40, width=55)
        self.loginL.configure(foreground="#000000")
        self.loginL.configure(font=font10)
        self.loginL.configure(relief="flat")
        self.loginL.configure(text='''Login''')
        self.loginL.configure(width=55)

        self.rID = ttk.Entry(self.rgLFrame)
        self.rID.place(relx=0.1, rely=0.45, relheight=0.07, relwidth=0.314)
        self.rID.configure(takefocus="")
        self.rID.configure(cursor="ibeam")

        self.lID = ttk.Entry(self.rgLFrame)
        self.lID.place(relx=0.599, rely=0.367, relheight=0.07, relwidth=0.314)
        self.lID.configure(takefocus="")
        self.lID.configure(cursor="ibeam")

        self.lpass = ttk.Entry(self.rgLFrame)
        self.lpass.place(relx=0.599, rely=0.567, relheight=0.07, relwidth=0.314)
        self.lpass.configure(takefocus="")
        self.lpass.configure(cursor="ibeam")

        self.rButton = ttk.Button(self.rgLFrame,command=self.register)
        self.rButton.place(relx=0.15, rely=0.8, height=25, width=76)
        self.rButton.configure(takefocus="")
        self.rButton.configure(text='''Register''')

        self.LButton = ttk.Button(self.rgLFrame,command=self.toggleLoginUI)
        self.LButton.place(relx=0.648, rely=0.8, height=25, width=76)
        self.LButton.configure(takefocus="")
        self.LButton.configure(text='''Log In''')


