from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
root.geometry("300x200")
root.config(bg="red")
#functions-------------------------
def getData():
    data=C1.get()
    print(data) 

#widgets---------------------------
C1=Combobox(root,values=["red","green","blue","white","black"])
B1=Button(root,text="ok",command=getData)

#packs-----------------------------
C1.pack()
B1.pack()

root.mainloop()

