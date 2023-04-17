import requests
import os
url = "https://countriesnow.space/api/v0.1/countries/capital"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

# ---------- get data from API ------------------
dic=response.json()
details=dic["data"]
dic={}
name=[]
capital=[]
iso2=[]
iso3=[]
for i in range(len(details)):
    dic=details[i]
    name.append(dic["name"])
    capital.append(dic["capital"])
    iso2.append(dic["iso2"])
    iso3.append(dic["iso3"])
# ---------- write data in file --------------------
f=open("data.txt","w")
for i in range(len(name)):
    s=f"{name[i]},{capital[i]},{iso2[i]},{iso3[i]}\n"
    f.write(s)
f.close()
# ---------- main body -----------------
os.system("cls")
print("world wide countries details are ready...")
ask=input("search by country, capital, iso or end: ")
while ask!="end":
    if ask=="country":
        countryName=input("enter a country start by capital letter: ")
        if countryName in name:
            index=name.index(countryName)
            print(f"{name[index]},{capital[index]},{iso2[index]},{iso3[index]}")
    elif ask=="capital":
        capitalName=input("enter a capital start by capital letter: ")
        if capitalName in capital:
            index=capital.index(capitalName)
            print(f"{name[index]},{capital[index]},{iso2[index]},{iso3[index]}")
    elif ask=="iso":
        iso=input("enter a iso by capital letter: ")
        if iso in iso2:
            index=iso2.index(iso)
            print(f"{name[index]},{capital[index]},{iso2[index]},{iso3[index]}")
    else:
        print("invalid command recieved, try again!")
    print("any question?")  
    ask=input("search by country, capital, iso or end: ")






