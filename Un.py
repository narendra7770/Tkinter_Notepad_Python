import tkinter as tk
from tkinter import font
main=tk.Tk()
global check,check1,check2,color,check3
check = True
check1 = True
check2=True
color=True
check3=True
menu = tk.Menu()
main.geometry('480x360')
main.title("NOTEPAD EDITOR")
text=tk.Text(main)
text.pack(expand=True)
def action():
    global check
    
    if check:
        text.config(font="bold")
        check = False
    else:
        text.config(font=('',12,'normal'))
        check = True
def action1():
    global check1
    if check1:
        text.config(font=('',12,'italic'))
        check1 = False
    else:
        text.configure(font=('',12,'normal'))
        check1 = True

def action2():
    global check2
    if check2:
        text.config(font=('',12,'underline'))
        check2= False
    else:
        text.configure(font=('',12,'normal'))
        check2 = True 
def color():
    text.config(fg="blue")
    text.config(fg="red")

               
def action3():
    global check3
    if check3:
        text.config(font=('',12,'select'))
        check3= False
    else:
        text.configure(font=('',12,'normal'))
        check3= True
        
menu.add_command(label="Bold",command = action)
menu.add_command(label="Italic",command = action1)
menu.add_command(label="Underline",command = action2)
menu.add_command(label="Select",command = 3)
menu.add_command(label="color",command = color)

main.config(menu = menu)
main.mainloop()
