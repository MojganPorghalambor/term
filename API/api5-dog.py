from datetime import *
import requests
# لینک به صورت رندوم عکس سگ با ابعاد دلخواه برمیگرداند
tol=int(input("enter a length: "))
arz=int(input("enter a width: "))
url=f"https://place.dog/{tol}/{arz}"
#میخواهیم عکس ها را با زمان اجرای فایل نام گذاری کنیم که هر دفعه یک نام متفاوت داشته باشیم.
response=requests.get(url)

zaman=datetime.now()
fileName=f"{zaman.year}-{zaman.month}-{zaman.day}-{zaman.hour}-{zaman.minute}-{int(zaman.second)}.jpg"
with open(fileName,"wb") as f:
    f.write(response.content)