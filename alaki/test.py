kala=["goshi","moz","apple"]
ghimat=["1200","500","200"]
tedad=[3,4,9]
print(kala)
y=input("chi mikhai")

for i  in range(len(kala)):
    if  y==kala[i]:
        print(f"gheymat in kala {ghimat[i]} ast")
        jjj=int(input("chan ta mikhay: "))
        if jjj<=tedad[i]:
            print(jjj*ghimat[i])
            rams=8260
            a=int(input("enter your rams"))
            c=1
            while a!=rams:
                print("wrong number")
                a=int(input("enter rams"))
                if c==3:
                    print("erro")
                    break
                else:
                    c=c+1 
            cvv2=8901
            adad=int(input("enter your cvv2"))
            dd=1
            while adad!=cvv2:
                print("worn number")
                adad=int(input("enter cvv2"))
            if dd==3:
                print("erro")
                break
            else:
                dd=dd+1
            f=open("kharid.txt","w")
            f.write(str(y))
            f.write(str(jjj))
            f.close()
        else:
            print("kala be tedad kafi mojod nist")
    
else:
    print("mamnon az khridtan")
