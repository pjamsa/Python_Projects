import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
import time
import shutil
import os


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 215))
        self.master.title("Check files")
        self.master.configure(bg="lightgray")


        self.btn_add = tk.Button(self.master,width=12,height=1,text='Browse',command=lambda: pickFolder1(self))
        self.btn_add.grid(row=4,column=0,padx=(20,0),pady=(45,0),sticky=W)
        self.btn_add = tk.Button(self.master,width=12,height=1,text='Browse',command=lambda: pickFolder2(self))
        self.btn_add.grid(row=5,column=0,padx=(20,0),pady=(10,0),sticky=W)
        self.btn_open = tk.Button(self.master,width=12,height=2,text='Check File',command=lambda: checkFiles(self))
        self.btn_open.grid(row=6,column=0,padx=(20,0),pady=(10,0),sticky=W)
        

        self.txt_1 = tk.Entry(self.master,width=64)
        self.txt_1.grid(row=4,column=2,rowspan=1,columnspan=2,padx=(30,0),pady=(50,0),sticky=N+E+W)
        self.txt_2 = tk.Entry(self.master,width=64,text= '')
        self.txt_2.grid(row=5,column=2,rowspan=1,columnspan=2,padx=(30,0),pady=(10,0),sticky=N+E+W)

def pickFolder1(self):
    path1 = askdirectory(title='Select Folder')
    self.txt_1.insert(END, path1)



def pickFolder2(self):
    path2 = askdirectory(title='Select Folder') 
    self.txt_2.insert(END, path2)



""" Previous script written for previous step


    SECONDS_IN_DAY = 24 * 60 * 60
    source =  <insert path1> modified to coincide with current code
    destination =  <insert path2> modified to coincide with current code
    now = time.time()
    before = now - SECONDS_IN_DAY

def last_mod_time(files):
    return os.path.getmtime(files)

for files in os.listdir(source):
    source_files = os.path.join(source, files)
    if last_mod_time(source_files) > before:
        destination_files = os.path.join(destination, files)
        shutil.move(source_files, destination_files)
    
"""   




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
