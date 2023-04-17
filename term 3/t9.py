from tkinter import *
root=Tk()
root.geometry("250x200")
#functions--------------------
def getData():
    num1=int(E1.get())
    num2=int(E2.get())
    return num1,num2
    
def jam():
    num1,num2=getData()
    L3=Label(root,text=num1+num2)
    L3.grid(row=2,column=1)

def tafrigh():
    num1,num2=getData()
    L3=Label(root,text=num1-num2)
    L3.grid(row=2,column=1)    

def zarb():
    num1,num2=getData()
    L3=Label(root,text=num1*num2)
    L3.grid(row=2,column=1)

def taghsim():
    num1,num2=getData()
    L3=Label(root,text=num1/num2)
    L3.grid(row=2,column=1)

#widgets----------------------
L1=Label(root,text="num1",width=10,height=1)
E1=Entry(root)
L2=Label(root,text="num2")
E2=Entry(root)
L3=Label(root)
B1=Button(root,text="+",width=10,height=1,command=jam)
B2=Button(root,text="-",width=10,height=1,command=tafrigh)
B3=Button(root,text="*",width=10,height=1,command=zarb)
B4=Button(root,text="/",width=10,height=1,command=taghsim)


#packs------------------------
L1.grid(row=0,column=0)
E1.grid(row=0,column=1)
L2.grid(row=1,column=0)
E2.grid(row=1,column=1)
L3.grid(row=2,column=1)
B1.grid(row=3,column=0)
B2.grid(row=3,column=1)
B3.grid(row=4,column=0)
B4.grid(row=4,column=1)




root.mainloop()

