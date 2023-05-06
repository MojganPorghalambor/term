import time
from threading import Thread
def func1():
    for i in range(5):
        print(f"{i} bla bla bla")
        time.sleep(1)

def func2():
    for i in range(5):
        print(f"{i} hi bye hi bye")
        time.sleep(1)

def func3():
    for i in range(5):
        print(f"{i} sammi")
        time.sleep(1)


t1=Thread(target=func1)
t2=Thread(target=func2)

t1.start()
t2.start()
func3()

