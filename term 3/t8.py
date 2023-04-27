from tkinter import *
root=Tk()
#functions-------------
def begirData():
    name=E1.get()
    lastname=E2.get()
    phone=int(E3.get())
    print(phone)





#widgets----------------
L1=Label(root,text="Name:")
E1=Entry(root)
L2=Label(root,text="Last Name:")
E2=Entry(root)
L3=Label(root,text="Phone Number:")
E3=Entry(root)
B1=Button(root,text="ok",command=begirData)

#packs------------------
L1.grid(row=0,column=0)
E1.grid(row=0,column=1)
L2.grid(row=1,column=0)
E2.grid(row=1,column=1)
L3.grid(row=2,column=0)
E3.grid(row=2,column=1)
B1.grid(row=3,column=1)


root.mainloop()