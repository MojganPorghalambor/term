from ProjeAsciiType1 import myDic
# asccii code are in myDic and need to be complete
# enter a name to creat ascci code it

name=""
while name!="end":
    name=input("Enter your name: ")
    name=name.lower()
    if name=="end":
        break
    print()
    nameList=list(name)
    for letter in nameList:
        print(myDic[letter])