import sys
sys.path.append("..")
import tkinter as tk
import tkinter.ttk as ttk
from Controller.ForumFunctions import *
from View.discussionFrame import *


class searchDFrame:
    def discussionofForum(self,que):
        self.f2.destroy()
        d= discussionofForum(self.s,que)

    def __init__(self,top=None,q=None):
        self.s=top
        f=ForumFunctions
        result=f.getSearch(f,q)
        self.f2=tk.Frame(top)
        self.f2.pack(expand=True,fill='both')
        self.l=tk.Label(self.f2)
        self.l.pack(side=tk.LEFT)

        

        if result==1:
            self.l.configure(text="There are search related to this term")
        else:
            self.l.configure(text=result,font=(None,20))
            self.l.bind("<Button-1>",lambda e: self.discussionofForum(result))
        




