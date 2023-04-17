from tkinter import *
from tkinter import messagebox


root=Tk()
root.geometry("300x200")
root.config(bg="pink")
root.title("Tamrin 3")
root.resizable(0,1)
root.iconbitmap('home.ico')
#-------widgets-------

b1=Button(root,bg="yellow",text="login",fg="red")
b2=Button(root,bg="yellow",text="login",fg="red")




#-------pack----------
b1.pack()
b2.pack()



root.mainloop()
