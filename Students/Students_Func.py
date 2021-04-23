import os
from tkinter import *
import tkinter as tk
import sqlite3

import Students

conn = sqlite3.connect('Student_Tracking.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
    conn.commit()
conn.close








if __name__ == "__main__":
    pass
