import os
os.system("cls")
do=input("Enter show, add, delete, end: ")

while do!="end":
    if do=="show":
        f=open("note.txt","r")
        notes=f.readlines()
        for i in notes:
            print(i.strip("\n"))
    elif do=="add":
        f=open("note.txt","a")
        todo=input("enter sth to add: ")
        time=input("enter time: ")
        f.write(f"{todo}\n")
        f.write(f"{time}\n")
    
    elif do=="delete":
        finder=False
        Delete_item=input("Enter Item to delete: ")
        f=open("note.txt","r")
        notes=f.readlines()
        for i in range(0,len(notes),2):
            if Delete_item == notes[i].strip("\n"):
                finder=True
                del notes[i+1]
                del notes[i]
                break
        print(notes)    
        if finder==False:
            print("item not found")
        else:
            f=open("note.txt","w")
            for i in notes:
                f.write(f"{i}")
            print("item deleted")
       
    else:
        print("try again!")
    do=input("Enter show, add, delete, end: ")
f.close()

