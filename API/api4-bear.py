from datetime import *
import requests
# لینک به صورت رندوم عکس خرس با ابعاد دلخواه برمیگرداند
tol=int(input("Enter a lenght: "))
arz=int(input("enter a width: "))
url=f"https://placebear.com/{tol}/{arz}"
response=requests.get(url)
#میخواهیم عکس ها را با زمان اجرای فایل نام گذاری کنیم که هر دفعه یک نام متفاوت داشته باشیم.
zaman=datetime.now()
fileName=f"{zaman.year}-{zaman.month}-{zaman.day}-{zaman.hour}-{zaman.minute}-{int(zaman.second)}.jpg"
with open(fileName,"wb") as f:
    f.write(response.content)
