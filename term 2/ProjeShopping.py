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


def show():
    print("-"*10,"samsung","-"*10)
    for i in sam.keys():
       print(f"{i}:\t {sam[i]}")
    print("-"*10,"apple","-"*10)
    for i in apple.keys():
        print(f"{i}:\t {apple[i]}") 

def buy():
    global TotalPrice
    item=input("choose an item: ")
    if item in sam.keys():
        TotalPrice=TotalPrice+sam[item]
    elif item in apple.keys():
        TotalPrice=TotalPrice+apple[item]
    factor.append(item)

def pay():
    print("-"*10,"yout shopping list","-"*10)
    for i in factor:
        if i in sam.keys():
            print("\t",i,":\t",sam[i])
        if i in apple.keys():
            print("\t",i,":\t",apple[i])
    
    print("-"*40)
    print(f"\ttotalprice is {TotalPrice}")    

def employe():
    s=open("sign up.txt","a")
    name=input("Enter your name:")
    phonenumber=input("Enter your namber")
    single=f"{name}\t{phonenumber}"
    s.write(single)
    s.close()
#----------main code-------
TotalPrice=0
factor=[]
print("welcome to our shop")
todo=input("how could i help you? enter buy/employe ")
while todo!="end":
    if todo=="buy":
        show()
        buy()
    elif todo=="pay":
        pay()
    elif todo=="employe":
        employe()
    else:
        print("try again")
    todo=input("how could i help you? enter buy/employe/pay/end ")

