import sys
sys.path.append("..")
import tkinter as tk
import tkinter.ttk as ttk
from View.discussionFrame import *
from Controller.ForumFunctions import *


class discussionofForum:
    def home(self):
        self.dff.destroy()
        self.df=discussionFrame(self.tf)

    def on_configure(self,event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas1
        self.canvas1.configure(scrollregion=self.canvas1.bbox('all'))
    
    def refreshf(self):
        l=ForumFunctions
        self.list=l.getAnswersList(l,self.q)
        self.ranswers=l.getAnswers(l,self.q)
        
        for i in range(0,self.list):
            
            # --- add widgets in frame ---

            self.label_widgets.append(ttk.Label(self.forumFrame,text=self.ranswers[i],font=(None,10)))
            #task_style_choice = divmod(len(self.label_widgets), 2)
            #my_scheme_choice = self.colour_schemes[task_style_choice]
            self.label_widgets[-1].grid(row= i+1, column =0, sticky='e', padx=10, pady=10)
            #self.label_widgets[-1].configure(bg=my_scheme_choice["bg"])
            #self.label_widgets[-1].configure(fg=my_scheme_choice["fg"])

            

    def addDiscussion(self,que):
        answer = self.task_create.get(1.0,tk.END).strip()
        l=ForumFunctions
        
        l.insertAnswers(l,que,answer)

        self.task_create.delete(1.0, tk.END)
        self.refreshf()

    def __init__(self,top=None,que=None):
        self.tf=top
        self.dff=tk.Frame(self.tf)
        self.dff.pack(expand=True, fill='both')
        self.home=ttk.Button(self.dff,text="Home",command=self.home)
        self.home.pack()
        self.canvas1=tk.Canvas(self.dff)
        self.canvas1.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
        self.q=que
        
        self.forumFrame = ttk.Frame(self.canvas1)
        self.canvas1.create_window((0,20), window=self.forumFrame, anchor='w')

        self.scroll=tk.Scrollbar(self.dff,command=self.canvas1.yview)
        self.scroll.pack(side=tk.RIGHT,fill='y')
        
        self.task_create = tk.Text(top, height=2, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill='x')
        self.task_create.focus_set()
        self.task_create.bind("<Return>", lambda e : self.addDiscussion(self.q))

        self.canvas1.configure(yscrollcommand = self.scroll.set)
        self.canvas1.bind('<Configure>', self.on_configure)

        self.label_widgets=[]
        
        self.refreshf()
        
        
        





