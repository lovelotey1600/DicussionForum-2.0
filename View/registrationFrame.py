import sys
sys.path.append("..")
import tkinter as tk
import re
import tkinter.ttk as ttk
from tkinter import messagebox
from Controller.signupIN import *

class registrationFrame:
    def rgstrU(self):
        p1="^[a-zA-Z0-9\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$"
        if self.uName.get()=="" or self.uEmail.get()=="" or self.uPass.get()=="" or self.uRP.get()=="":
            messagebox.showinfo("Registration","You cannot leave any of these fields empty.")   
        else:
            n=self.uName.get()
            ei=self.uEmail.get()
            if re.match(p1,ei):
                uh=self.uID.get()
                p=self.uPass.get()
                rp=self.uRP.get()
                if(p==rp):
            
                    self.uName.delete(0, 'end')
                    self.uEmail.delete(0, 'end')
                    self.uID.delete(0, 'end')
                    self.uPass.delete(0, 'end')
                    self.uRP.delete(0, 'end')
            
                    c=register
                    c.usrgstr(c,n.strip(),ei.strip(),uh.strip(),p.strip())
                else:
                    messagebox.showinfo("Registration","Passwords you entered didn`t match.")   
            else:
                messagebox.showinfo("Registration","Email you entered doesn`t follow correct format.\nYou should enter email like abc@email.com")   

    def __init__(self, top=None,u=None):
        font9 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        self.rgFrame = ttk.Frame(top)
        self.rgFrame.place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.499)
        self.rgFrame.configure(relief='groove')
        self.rgFrame.configure(borderwidth="2")
        self.rgFrame.configure(relief="groove")
        self.rgFrame.configure(width=385)

        self.registerL = ttk.Label(self.rgFrame)
        self.registerL.place(relx=0.4, rely=0.083, height=40, width=80)
        self.registerL.configure(foreground="#000000")
        self.registerL.configure(font=font9)
        self.registerL.configure(relief="flat")
        self.registerL.configure(text='''Register''')

        self.uEmail = ttk.Entry(self.rgFrame)
        self.uEmail.place(relx=0.55, rely=0.367, relheight=0.07, relwidth=0.365)
        self.uEmail.configure(width=146)
        self.uEmail.configure(takefocus="")
        self.uEmail.configure(cursor="ibeam")

        self.uName = ttk.Entry(self.rgFrame)
        self.uName.place(relx=0.55, rely=0.267, relheight=0.07, relwidth=0.365)
        self.uName.configure(width=146)
        self.uName.configure(takefocus="")
        self.uName.configure(cursor="ibeam")

        self.uID = ttk.Entry(self.rgFrame)
        self.uID.place(relx=0.55, rely=0.483, relheight=0.07, relwidth=0.365)
        self.uID.insert(0,u)
        self.uID.configure(width=146)
        self.uID.configure(takefocus="")
        self.uID.configure(cursor="ibeam")

        self.rgstB = ttk.Button(self.rgFrame)
        self.rgstB.place(relx=0.4, rely=0.867, height=25, width=76)
        self.rgstB.configure(takefocus="")
        self.rgstB.configure(text='''Register''')

        self.uPass = ttk.Entry(self.rgFrame)
        self.uPass.place(relx=0.55, rely=0.583, relheight=0.07, relwidth=0.365)
        self.uPass.configure(width=146)
        self.uPass.configure(takefocus="")
        self.uPass.configure(cursor="ibeam")

        self.uRP = ttk.Entry(self.rgFrame)
        self.uRP.place(relx=0.55, rely=0.7, relheight=0.07, relwidth=0.365)
        self.uRP.configure(width=146)
        self.uRP.configure(takefocus="")
        self.uRP.configure(cursor="ibeam")

        self.TLabel1 = ttk.Label(self.rgFrame)
        self.TLabel1.place(relx=0.125, rely=0.267, height=19, width=95)
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Enter User Name :''')
        self.TLabel1.configure(width=95)

        self.TLabel2 = ttk.Label(self.rgFrame)
        self.TLabel2.place(relx=0.125, rely=0.367, height=19, width=115)
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Enter User Email ID:''')
        self.TLabel2.configure(width=115)

        self.TLabel3 = ttk.Label(self.rgFrame)
        self.TLabel3.place(relx=0.125, rely=0.483, height=19, width=85)
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''Enter User ID:''')
        self.TLabel3.configure(width=85)

        self.TLabel4 = ttk.Label(self.rgFrame)
        self.TLabel4.place(relx=0.125, rely=0.583, height=19, width=95)
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(text='''Enter Password :''')
        self.TLabel4.configure(width=95)

        self.TLabel5 = ttk.Label(self.rgFrame)
        self.TLabel5.place(relx=0.125, rely=0.7, height=19, width=115)
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(text='''Re -enter Password:''')
        self.TLabel5.configure(width=115)





