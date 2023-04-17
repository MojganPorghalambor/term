from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
# function------
def showpic():
    if c1.get()=="ice cream":
        logo=PhotoImage(file="1.png")
    elif c1.get()=="love":
        logo=PhotoImage(file="2.png")
    elif c1.get()=="hello":
        logo=PhotoImage(file="3.png")
    elif c1.get()=="water":
        logo=PhotoImage(file="4.png")
    elif c1.get()=="bye":
        logo=PhotoImage(file="5.png")
    l1.config(image=logo)
    root.mainloop()

#widgets-------------
c1=Combobox(root,values=["ice cream","love","hello","water","bye"],state="readonly")
c1.set("----")
b1=Button(root,text="show",command=showpic)
l1=Label(root)
#pack-----------
c1.pack()
b1.pack()
l1.pack()

#end of code---------
root.mainloop()