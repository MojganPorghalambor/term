from tkinter import *

def getData():
    global userName,password
    userName=e1.get()
    password=e2.get()
    check()
def check():
    if userName=="admin" and password=="1234":
        print("log in succefully")
    else:
        print("log in fail")
        
root=Tk()
root.geometry("300x200")
root.config(bg="pink")
root.title("Tamrin 3")

#-------widgets-------
l1=Label(root,bg="pink",fg="darkgreen",text="user name:")
e1=Entry()
l2=Label(root,bg="pink",fg="gray",text="password:")
e2=Entry()

b1=Button(root,bg="yellow",text="login",fg="red",command=getData)



#-------pack----------
l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()



root.mainloop()