from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
foodList=["pizza","burger","sandwich","salad","coca"]
foodPrice=[10000,15000,7000,12000,1000]
# functions---------
def getData():
    number=s1.get()
    for i in range(len(foodList)):
        if foodList[i]==c1.get():
            price=foodPrice[i]

    total=price*int(number)
    print(total)

# widgets-----------
l1=Label(root,text="food name:",width=10)
c1=Combobox(root,values=foodList,state="readonly",width=20)
c1.set("choose one")
l2=Label(root,text="number",width=10)
s1=Spinbox(root,from_=1,to=10,width=20)
b1=Button(root,text="finish",width=10,bg="yellow",command=getData)

#grids--------------
l1.grid(row=0,column=0)
c1.grid(row=0,column=1)
l2.grid(row=1,column=0)
s1.grid(row=1,column=1)
b1.grid(row=2,column=1)

#end of code--------
root.mainloop()
