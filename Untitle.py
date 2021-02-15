import tkinter as tk
main_app=tk.Tk()
main_app.geometry("800x600")
main_app.title("notepad")
def Bold():
    text.config(font=("bold"))
    

    


btn=tk.Button(text="bold",command=Bold)
btn.pack()




text=tk.Text()
text.pack(expand=True)

main_app.mainloop()