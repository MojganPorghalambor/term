from tkinter import *
root=Tk()
root.geometry("300x300")
root.title("t3")
root.config(bg="yellow")

def begir_data():
    matn=E1.get()
    L2=Label(root,bg="yellow",text=matn)
    L2.pack()

#widgets----------
L1=Label(root,bg="yellow",text="label aval")
E1=Entry()
B1=Button(root,bg="red",text="msg box",fg="white",command=begir_data)



#packs------------
L1.pack()
E1.pack()
B1.pack()

root.mainloop()