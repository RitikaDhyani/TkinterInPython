import tkinter as tk
b=tk.Tk()
tk.Label(text="HI programmers",fg="pink",bg="red").pack()
b.title("tkinter button")
def show():
    print("This is how we code")
button=tk.Button(b,text="button",command=show,bg="blue").pack()
b.mainloop()
