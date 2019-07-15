import sys
sys.path.append("..")
import tkinter as tk
import tkinter.ttk as ttk
from Controller.ForumFunctions import *
from View.discussionofForum import *
class discussionFrame:
    def on_configure(self,event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def discussionofForum(self,que):
        self.f.destroy()
        d= discussionofForum(self.t,que)

    def refresh(self):
        l=ForumFunctions
        self.list=l.getList1(l)
        self.questions=l.getQuestions(l)
        
        for i in range(0,self.list):
            
            # --- add widgets in frame ---

            self.label_widgets.append(ttk.Label(self.forumFrame,text=self.questions[i],font=(None,20)))
            self.label_widgets[-1].grid(row= i+1, column =0, sticky='e', padx=10, pady=10)
            self.qu=self.label_widgets[-1].cget("text")
            self.label_widgets[-1].bind("<Button-1>",lambda e: self.discussionofForum(self.qu))

    def __init__(self, top=None):
        
        self.t=top
        self.f=tk.Frame(self.t)
        self.f.pack(expand=True, fill='both')
        self.canvas=tk.Canvas(self.f)
        self.canvas.place(x=0,y=10)
        

        self.scroll=tk.Scrollbar(self.f,command=self.canvas.yview)
        self.scroll.pack(side=tk.RIGHT,fill='y')
        

        self.canvas.configure(yscrollcommand = self.scroll.set)
        self.canvas.bind('<Configure>', self.on_configure)

        self.label_widgets=[]
        self.forumFrame = ttk.Frame(self.canvas)
        self.canvas.create_window((0,20), window=self.forumFrame, anchor='w')
        self.refresh()





