from tkinter import *
root=Tk()

root.geometry("300x300")
root.config(bg="blue")
root.title("t5")

#functions-----
def new_msg():
    page=Toplevel()
    page.config(bg="red")
    page.geometry("100x100")
    l1=Label(page,bg="green",text=e1.get())
    l1.pack()


#widgets-------
L1=Label(root,bg="blue",text="enter button for new msg",fg="white")
B2=Button(root,bg="red",text="click me!",command=new_msg)
e1 = Entry(root)


#packs---------
L1.pack()
B2.pack()
e1.pack()




root.mainloop()