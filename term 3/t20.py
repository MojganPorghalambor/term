from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
root.geometry("250x200")
root.config(bg="yellow")
foodList=["fesenjon","baghali polo","joje kabab"]
priceList=[10000,5000,30000]
tedadList=[1,2,3,4,5,6]

#functions------------
def getData():
    food=C1.get()
    number=int(C2.get())
    index=foodList.index(food)
    price=number*priceList[index] 
    print(price)   
    L3=Label(root,bg="yellow",text=price)
    L3.grid(row=2,column=1)

#widgets--------------
L1=Label(root,text="food name",bg="yellow",width=10,height=2)
C1=Combobox(root,value=foodList)
L2=Label(root,text="number",bg="yellow",width=10,height=2)
C2=Combobox(root,values=tedadList)
L3=Label(root,bg="yellow")
B1=Button(root,text="serve",command=getData)

#grids-----------------
L1.grid(row=0,column=0)
C1.grid(row=0,column=1)
L2.grid(row=1,column=0)
C2.grid(row=1,column=1)
L3.grid(row=2,column=1)
B1.grid(row=3,column=0,columnspan=2,sticky="news",padx=20,pady=10)

#end of code ----------
root.mainloop()