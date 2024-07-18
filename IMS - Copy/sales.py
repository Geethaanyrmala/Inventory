from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import sqlite3

class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Sales Info")
        self.root.geometry("1175x650+320+115")
        self.root.config(bg="#EEE8EC")
        self.root.focus_force()
        self.root.resizable(False,False)
        
if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()