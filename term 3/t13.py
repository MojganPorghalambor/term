from tkinter import *
root=Tk()

#function------------
def show():
    ax=PhotoImage(file="2.png")
    l1.config(image=ax)
    root.mainloop()

#widgets-------------
l1=Label(root)
b1=Button(root,text="click me",command=show)

#grids----------
l1.grid()
b1.grid()


#end of program------
root.mainloop()
