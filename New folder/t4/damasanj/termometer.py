from tkinter import *

class Termometer():
    def __init__(self, root, name = 'Termometer', liquid_color='red', solid_color='bisque', temp=20, **kwargs):
        self.root = root
        self.name = name
        self.liquid_color = liquid_color
        self.solid_color = solid_color
        self.temp = IntVar()
        self.temp.set(temp)
        self.frame = LabelFrame(self.root, text=self.name, width=100, height=160)
        self.spinbox = Spinbox(self.frame, textvariable=self.temp, width=3, state='readonly', command=self.change, from_=0, to=100, **kwargs)

        self.houses = []
        for i in range(100):
            h = Label(self.frame, **kwargs)
            self.houses.append(h)
        # self.spinbox.pack(side='bottom')
        self.spinbox.place(x=20, y=115, width=60, height=20)
        # self.spinbox.grid(row=101, column=2)
        for i in range(100):
            self.houses[i].place(x=46,y=(100-i),height=1, width=4)
        for i in range (10, 100, 20):
            Label(self.frame, text=i, bg=solid_color, font=('', 8)).place(x=27, y=93-i)
        for i in range (0, 100, 20):
            Label(self.frame, text=i, bg=solid_color, font=('', 8)).place(x=52, y=93-i)
        self.change()

    def change(self):
        t = self.temp.get()
        for i in range(100):
            if i < t:
                self.houses[i]['bg']=self.liquid_color
            elif i >= t:
                self.houses[i]['bg']='gray'
            self.root.update()
    
    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
    def place(self, x=0, y=0, width=100, height=160):
        self.frame.place(x=x, y=y, width=width, height=height)

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def __str__(self):
        return self.spinbox.get()
    def get_temp(self):
        return self.spinbox.get()
    def set_temp(self, new_temp):
        self.temp.set(new_temp)
        self.change()


if __name__ == "__main__":
    root = Tk()
    t1 = Termometer(root, name="Damasanj 1", liquid_color='purple', solid_color='khaki', font=('Calibri', 12))
    t2 = Termometer(root, name="Termometer 2", liquid_color='red', font=('Serif', 12), temp=60)
    # t1.pack(side='left', expand=1, fill='y')
    # t2.pack(side='left', expand=1, fill='y')
    t1.grid(row=1, column=1)
    t2.grid(row=1, column=2)
    # t1.place(x=10, y=10)
    # t2.place(x=110, y=10)
    root.mainloop()
