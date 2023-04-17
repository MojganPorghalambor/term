from datetime import *
import requests
#این لینک به صورت رندوم عکس از قهوه برمیگرداند
response=requests.get("https://coffee.alexflipnote.dev/random.json")
data=response.json()
url=data["file"]
getPic=requests.get(url)
#میخواهیم عکس ها را با زمان اجرای فایل نام گذاری کنیم که هر دفعه یک نام متفاوت داشته باشیم.
zaman=datetime.now()
fileName=f"{zaman.year}-{zaman.month}-{zaman.day}-{zaman.hour}-{zaman.minute}-{int(zaman.second)}.jpg"
with open (fileName,"wb")as f:
    f.write(getPic.content)
