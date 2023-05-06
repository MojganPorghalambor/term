from tkinter import *

class Termometer():
    def __init__(self,root,title,bg_color,temp_color):
        self.root = root
        self.title= title
        self.bg_color = bg_color
        self.temp_color= temp_color
        self.frame = LabelFrame(self.root, width=100, height=160)
        self.temp_box= Spinbox(self.frame, from_=0, to=100, width=5)
        self.temp_box.place(x=20, y=130)
        self.set_title()
        self.create_right_numbers()
        self.houses=[]
        self.create_houses()

    def frame_grid(self,row, col):
        self.frame.grid(row=row, column=col)

    def set_title(self):
        t=Label(self.frame, text=self.title, font=('', 8))
        t.place(x=0, y=0)
    
    def create_right_numbers(self):
        for i in range (10, 100, 20):
            Label(self.frame, text=i,  font=('', 8)).place(x=27, y=110-i)
        for i in range (0, 100, 20):
            Label(self.frame, text=i,  font=('', 8)).place(x=52, y=110-i)
    
    def create_houses(self):
        temp = 50
        for i in range(100):
            l=Label(self.frame, bg="red")
            self.houses.append(l)

        for i in range(100):
            self.houses[i].place(x=45, y=(100-i))


    
  



    
