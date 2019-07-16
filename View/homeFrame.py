import sys
sys.path.append("..")
import tkinter as tk
import tkinter.ttk as ttk
from View.startDFrame import *
from View.discussionFrame import *
from View.searchDFrame import *

class homeFrame:
    def startDFrame(self):
        self.df.f.destroy()
        del(self.df)
        self.TLabelframe1.configure(text='''Start a new Discussion''')
        sd=startDFrame(self.TLabelframe1)

    def forumDisplay(self):
        self.df=discussionFrame(self.TLabelframe1)

    
    def search(self):
        self.df.f.destroy()
        del(self.df)
        self.TLabelframe1.configure(text='''Search Discussion''')
        ques=self.searchT.get("1.0",'end-1c')
        search=searchDFrame(self.TLabelframe1,ques)

    def searchBarDisplay(self):
        
        self.searchT = tk.Text(self.sideFrame)
        self.searchT.place(relx=0.15, rely=0.333, relheight=0.1, relwidth=0.35)
        self.searchT.configure(background="white")
        self.searchT.configure(font="TkTextFont")
        self.searchT.configure(foreground="black")
        self.searchT.configure(highlightbackground="#d9d9d9")
        self.searchT.configure(highlightcolor="black")
        self.searchT.configure(insertbackground="black")
        self.searchT.configure(selectbackground="#c4c4c4")
        self.searchT.configure(selectforeground="black")
        self.searchT.configure(width=10)
        self.searchT.configure(wrap="word")

        self.searchB = ttk.Button(self.sideFrame,command=self.search)
        self.searchB.place(relx=0.55, rely=0.333, height=60, width=52)
        self.searchB.configure(takefocus="")
        self.searchB.configure(text='''S''')

    def __init__(self,top=None):
        self.sideFrame = ttk.Frame(top)
        self.sideFrame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.25)
        self.sideFrame.configure(relief='groove')
        self.sideFrame.configure(borderwidth="2")
        self.sideFrame.configure(relief="groove")
        self.sideFrame.configure(width=190)

        self.startD = ttk.Button(self.sideFrame,command=self.startDFrame)
        self.startD.place(relx=0.15, rely=0.083, height=25, width=132)
        self.startD.configure(takefocus="")
        self.startD.configure(text='''Start a new Discussion''')

        #self.chatroomB = ttk.Button(self.sideFrame,command=self.home)
        #self.chatroomB.place(relx=0.15, rely=0.167, height=25, width=132)
        #self.chatroomB.configure(takefocus="")
        #self.chatroomB.configure(text='''Home''')

        self.searchBarB = ttk.Button(self.sideFrame,command=self.searchBarDisplay)
        self.searchBarB.place(relx=0.15, rely=0.25, height=25, width=132)
        self.searchBarB.configure(takefocus="")
        self.searchBarB.configure(text='''Search for a Discussion''')

        self.exitB = ttk.Button(self.sideFrame,command=exit)
        self.exitB.place(relx=0.325, rely=0.875, height=25, width=70)
        self.exitB.configure(takefocus="")
        self.exitB.configure(text='''Exit''')
        
        self.TLabelframe1 = ttk.Labelframe(top)
        self.TLabelframe1.place(relx=0.25, rely=0.0, relheight=0.992
                , relwidth=0.749)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''Forum''')
        self.TLabelframe1.configure(width=600)

        self.forumDisplay()




