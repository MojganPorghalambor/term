from tkinter import *

root=Tk()

#functions------------
def show():
    photo=PhotoImage(file="1.png")
    l1=Label(root,image=photo)
    l1.grid()
    root.mainloop()

#widgets--------------
b1=Button(root,text="click me",command=show)

#grids-----------------
b1.grid()


root.mainloop()