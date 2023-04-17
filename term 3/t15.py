from tkinter import *
root=Tk()
#functions---------------
def get():
    print(zaban.get())
    print(gender.get())

# variables-------------
zaban=StringVar()
gender=StringVar()

#widgets----------------
l1=Label(root,text="language:")
r1=Radiobutton(root,text="english",value="eng",variable=zaban)
r2=Radiobutton(root,text="persian",value="fa",variable=zaban)
l2=Label(root,text="gender:")
r3=Radiobutton(root,text="girl",value="grl",variable=gender)
r4=Radiobutton(root,text="boy",value="boy",variable=gender,font=500)
b1=Button(root,text="submit",command=get)

#grids------------------
l1.grid(row=0,column=0)
r1.grid(row=0,column=1)
r2.grid(row=0,column=2)
l2.grid(row=1,column=0)
r3.grid(row=1,column=1)
r4.grid(row=1,column=2)
b1.grid(row=2,column=1)

root.mainloop()