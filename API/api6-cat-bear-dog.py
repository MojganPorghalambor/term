from datetime import *
import requests
ax=input("enter what would you like to see: cat, dog or bear? ")
while ax!="end":
    while ax!="cat" and ax!="dog" and ax!="bear":
        print("invalid input!")
        ax=input("enter what would you like to see: cat, dog or bear? ")
    if ax=="cat":
        site="https://placekitten.com/"
    elif ax=="bear":
        site="https://placebear.com/"
    elif ax=="dog":
        site=f"https://place.dog/"

    tol=int(input("enter a lenght: "))
    arz=int(input("enter a width: "))
    url=f"{site}/{tol}/{arz}"
    response=requests.get(url)

    zaman=datetime.now()
    fileName=f"{zaman.year}-{zaman.month}-{zaman.day}-{zaman.hour}-{zaman.minute}-{int(zaman.second)}.jpg"

    with open(fileName,"wb") as f:
        f.write(response.content)
        print("photo saved!")
    ax=input("enter what would you like to see: cat, dog, bear and end for finish... ")

