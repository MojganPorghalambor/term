sam = {
    "j4" : 1000,
    "A51" : 50000,
    "A72" : 30000
}

apple = {
    "se" : 1000,
    "i10" : 50000,
    "i12" : 30000
}
def employe(a):
    brand = a + ".txt"
    name = input("name: ")
    phone = input("phone number: ")
    f = open(brand,"a")
    f.write(f"name : {name} \t phone : {phone} \n")
    f.write("-------------------------------------------------- \n")
    f.close()

def show(a):
    if a =="sam" :
        samlist = sam.keys()
        for i in samlist:
            print(f" {i} : {sam[i]}")
    elif a =="apple" :
        applist = apple.keys()
        for i in applist:
            print(f" {i} : {apple[i]}")
    
def buy():

    