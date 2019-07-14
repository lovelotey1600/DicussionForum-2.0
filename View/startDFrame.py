import sys
sys.path.append("..")
import tkinter as tk
import tkinter.ttk as ttk

class startDFrame:
    def insertQuestion(self):
        ques=self.questionT.get("1.0",'end-1c')
        ans=self.answerT.get("1.0",'end-1c')
        f=ForumFunctions
        f.createQuestion(f,ques,ans)

    def __init__(self,top=None):
        self.questionT = tk.Text(top)
        self.questionT.place(relx=0.4, rely=0.134, relheight=0.108, relwidth=0.44
                , bordermode='ignore')
        self.questionT.configure(background="white")
        self.questionT.configure(font="TkTextFont")
        self.questionT.configure(foreground="black")
        self.questionT.configure(highlightbackground="#d9d9d9")
        self.questionT.configure(highlightcolor="black")
        self.questionT.configure(insertbackground="black")
        self.questionT.configure(selectbackground="#c4c4c4")
        self.questionT.configure(selectforeground="black")
        self.questionT.configure(width=264)
        self.questionT.configure(wrap="word")

        self.answerT = tk.Text(top)
        self.answerT.place(relx=0.083, rely=0.387, relheight=0.427
                , relwidth=0.773, bordermode='ignore')
        self.answerT.configure(background="white")
        self.answerT.configure(font="TkTextFont")
        self.answerT.configure(foreground="black")
        self.answerT.configure(highlightbackground="#d9d9d9")
        self.answerT.configure(highlightcolor="black")
        self.answerT.configure(insertbackground="black")
        self.answerT.configure(selectbackground="#c4c4c4")
        self.answerT.configure(selectforeground="black")
        self.answerT.configure(width=464)
        self.answerT.configure(wrap="word")

        self.submitQ = ttk.Button(top,command=self.insertQuestion)
        self.submitQ.place(relx=0.375, rely=0.882, height=25, width=110
                , bordermode='ignore')
        self.submitQ.configure(takefocus="")
        self.submitQ.configure(text='''Submit your Query''')

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.083, rely=0.151, height=39, width=165
                , bordermode='ignore')
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Enter the title to your Query :''')
        self.TLabel1.configure(width=165)

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.083, rely=0.336, height=19, width=145
                , bordermode='ignore')
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Elaborate your Problem:''')
        self.TLabel2.configure(width=145)





