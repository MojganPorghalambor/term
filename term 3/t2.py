from tkinter import *
#-------functions-----
def begir_data():
    name=e1.get()
    lname=e2.get()
    phone=int(e3.get())
   # print(type(name)," ",lname," ",type(phone))


root=Tk()
root.geometry("250x300")
root.config(bg="orange")
root.title("My App")
#-------widgets---------
Label1=Label(root,text="name:",bg="orange")
Label2=Label(root,text="last name:",bg="orange")
Label3=Label(root,text="phone:",bg="orange")
Label4=Label(root,bg="orange")
e1=Entry()
e2=Entry()
e3=Entry()

save=Button(root,text="save",command=begir_data)

#-------pack------------
Label1.pack()
e1.pack()
Label2.pack()
e2.pack()
Label3.pack()
e3.pack()
Label4.pack()
save.pack()







#-------end--------------
root.mainloop()