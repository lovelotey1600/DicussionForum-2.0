import sys
sys.path.append("..")
import tkinter as tk
import tkinter.ttk as ttk
from View.loginRFrame import *

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = mainWindow (root)
   #mainFrame_support.init(root, top)
    root.mainloop()

def destroy_mainWindow():
    global w
    w.destroy()
    w = None

w = None

class mainWindow:
    def __init__(self, top=None):
        
        top.geometry("801x596+380+150")
        top.title("Discussion Forum 2.0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.mainframe = ttk.Frame(top)
        self.mainframe.place(relx=0.0, rely=0.0, relheight=1.007, relwidth=1.0)
        self.mainframe.configure(relief='groove')
        self.mainframe.configure(relief="groove")
        self.mainframe.configure(width=870)

        w= loginRFrame (self.mainframe)

if __name__ == '__main__':
    vp_start_gui()










