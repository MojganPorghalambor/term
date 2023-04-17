from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
root=Tk()
operatorList=["Irancell","hamrah aval","talia","rightel","shatel"]
sharjList1=[1000,2000,5000,"enter a price:"]
sharjList2=[5000,10000,20000,50000]
# function--------
def data(e):
    dataa=c1.get()
    if dataa in ["Irancell","hamrah aval"]:
        c2['values']=sharjList1
    else:
        c2['values']=sharjList2

def data2(e):
    dataaa=c2.get()
    if dataaa=="enter a price:":
        e1.grid(row=1,column=2)
    else:
        e1.grid_forget()

def getData():
    num=c2.get()
    if num=="enter a price:":
        num=e1.get()
    num=int(num)
    price=num*int(s1.get())
    ans=messagebox.askyesno("final price",f"your final price is {price}, are you sure?")
    if ans==True:
        print(price)

#widgets----------
l1=Label(root,text="Operator: ")
c1=Combobox(root,values=operatorList,state="readonly")
c1.set("choose one:")
c1.bind("<<ComboboxSelected>>",data)
l2=Label(root,text="Price:")
c2=Combobox(root,state="readonly")
c2.set("choose one:")
c2.bind('<<ComboboxSelected>>',data2)
e1=Entry(root)
l3=Label(root,text="How many:")
s1=Spinbox(root,from_=1,to=10,state="readonly")
b1=Button(root,text="Buy",command=getData)

#grids------------
l1.grid(row=0,column=0)
c1.grid(row=0,column=1)
l2.grid(row=1,column=0)
c2.grid(row=1,column=1)
l3.grid(row=2,column=0)
s1.grid(row=2,column=1)
b1.grid(row=3,column=1)

#end of code------
root.mainloop()