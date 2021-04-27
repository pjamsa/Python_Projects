import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import webbrowser

### opens file to edit
def open_file(): 
    filepath = askopenfilename(
        filetypes=[("HTML Files", "*.html")]
    )
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    
### saves file to computer
def save_file():
    filepath = asksaveasfilename(
        defaultextension="html",
        filetypes=[("HTML Files", "*.html")],
    )
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    
##opens browser
def goBrowser():
    webbrowser.open('C:/Users/paul_/Documents/Python_Projects/Python Challenges/Summer_Sale.html')


window = tk.Tk()
window.title("Customize Webpage")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)  
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_browser =tk.Button(fr_buttons, text="Open Browser", command=goBrowser)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_browser.grid(row=2,column= 0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")





window.mainloop()
