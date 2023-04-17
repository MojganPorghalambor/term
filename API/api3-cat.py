from datetime import *
import requests
# لینک به صورت رندوم عکس گربه با ابعاد دلخواه برمیگرداند
tol=int(input("enter a lenght: "))
arz=int(input("enter a width: "))
url=f"https://placekitten.com/{tol}/{arz}"
response=requests.get(url)
#میخواهیم عکس ها را با زمان اجرای فایل نام گذاری کنیم که هر دفعه یک نام متفاوت داشته باشیم.
zaman=datetime.now()
fileName=f"{zaman.year}-{zaman.month}-{zaman.day}-{zaman.hour}-{zaman.minute}-{int(zaman.second)}.jpg"
with open(fileName,"wb") as f:
    f.write(response.content)
