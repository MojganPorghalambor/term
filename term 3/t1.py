from tkinter import *
root=Tk()
root.geometry("600x400")
root.config(bg="yellow")
root.title("My App")

#widgets-------------
label1=Label(root,text="this is a test!",bg="orange")
label2=Label(root,text="test2",bg="red")

inp=Entry()
but=Button(root,text="ok")


#pack----------------
label1.pack()
label2.pack()
num1=inp.pack()
but.pack()

#end code------------
root.mainloop()