import turtle
import random
import os
# ----------
# bg details 
# # s = turtle.getscreen()
# # laki=turtle.Turtle()
# # laki.shape("dog")
# # laki.circle(20)
# s=turtle.Screen()
# s.screensize(10,10)
# s.bgcolor("#7ca8eb")
# s.title("haye")
# # name=s.textinput("hellifull", "حالت چطوره")
# -------------------
# snowflake

# t=turtle.Turtle()
# t.shape("classic")
# t.pencolor("#0049b8")
# t.shapesize(5)
# for i in range(8):
#     t.fd(100)
#     t.backward(50)
#     t.rt(45)
#     t.fd(30)
#     t.backward(30)
#     t.lt(90) 
#     t.fd(30)
#     t.backward(30)
#     t.lt(135)
#     t.fd(50)
#     t.rt(135)
# turtle.done()
# ---------------------
# circle circle
# t=turtle.Turtle()
# t.shape("classic")
# t.pencolor("#0049b8")
# for i in range(20,70,5):
#     t.circle(i)
# turtle.done()
# ----------------------
# t=turtle.Turtle()
# t.shape("classic")
# t.pencolor("#0049b8")
# for i in range(50,200):
#     t.circle(i)
#     t.lt(92)
# turtle.done()
# ---------------
# t=turtle.Turtle()
# for i in range(4):
#     t.fd(100)
#     for j in range(4):
#         t.left(90)
#         t.fd(20)
    
#     t.left(90)
# turtle.done()
# ---------------------
# t=turtle.Turtle()
# r=random.randint(50,100)
# for i in range(50,r,5):
#     for j in range(50,r,5):
#         t.circle(j)
#     t.lt(30)
# turtle.done()
# -----------------
# t=turtle.Turtle()
# print(t.stamp())
# t.fd(100)
# t.stamp()
# t.fd(100)
# turtle.done()
# -------------------
#برنامه ای که یک چیزی در فایل بنویسد و بخواند
# f=open("test.txt","w")
# f.write("this is a test! \n")
# f.close()
# come=input("would you like write or read? ")
# if come=="write":
#     f=open("test.txt","a")
#     inn=input("what should i write? ")
#     f.write(inn)
#     f.close()
# elif come=="read":
#     f=open("test.txt","r")
#     print(f.read())
#     f.close()
# else:
#    print("try again")
#---------------------
#برنامه ای که به اسم کاربر فایل بسازد
# file_name=input("whats your name? ")
# f=open(file_name+".txt","w")
# f.close()
#---------------------
# #log in register
# activity=input("log in or register? ")
# if activity=="log in":
#     file_name=input("whats your name? ")
#     f=open(file_name+".txt","r")
#     password=input("whats your password? ")
#     if f.read()==password:
#         print("you logged in succefully!")
#     else:
#         print("oh no oh no oh no no no no")

# elif activity=="register":
#     file_name=input("whats your name? ")
#     f=open(file_name+".txt","w")
#     password=input("whats your password? ")
#     f.write(password)
#     f.close()

# else:
#     print("try again!")
#-----------------------
# log in register with os checking
# file_list=os.listdir()
# activity=input("log in or register? ")
# if activity=="log in":
#     file_name=input("whats your name? ")+".txt"
#     if file_name in file_list:
#         f=open(file_name,"r")
#         password=input("whats your password? ")
#         if f.read()==password:
#             print("you log in succefully!")
#         else:
#             print("oh no oh no oh no no no no")
#     else:
#         print("this name is not found!")

# elif activity=="register":
#     file_name=input("whats your name? ")+".txt"
#     while file_name in file_list:
#          file_name=input("this name is already existing, choose another name? ")+".txt"
#     f=open(file_name,"w")
#     password=input("whats your password? ")
#     f.write(password)
#     print("your account created!")
#     f.close()

# else:
#     print("try again!")
#-----------------------
# از کاربر سوال بپرسه که میخواد لوگ این کنه یا رجیستر 
# اگر ثبت نام را انتخاب کرد از او نام کاربری و رمز عبور دریافت کند و در یک فایل ذخیره کند.
# اگر لاگین انتخاب کردمجددا از او نام کاربری و رمز عبور بپرسد و با اطلاعات داخل فایل مقایسه کند
#  اگر هردو درست بود پیام خوش آمد گویی چاپ کند.
# todo=input("register or login: ")
# if todo=="login":
#     f=open("poulstar.txt","r")
#     detail=f.readlines()
#     id=input("whats your name? ")
#     # detail[0]=detail[0].strip("\n")
#     # print(detail)
#     if id==detail[0].strip("\n"):
#         passs=input("whats your password? ")
#         if passs==detail[1]:
#             print("welcome to your account")
#     else:
#         print("your account not found")

# elif todo=="register":
#     f=open("poulstar.txt","w")
#     name=input("whats your name? ")
#     f.write(name)
#     f.write("\n")
#     password=input("whats your password?")
#     f.write(password)

# else:
#     print("unknown command! try again!")
# f.close()
# ------------------------
# lissst=[111,1212,1223,3434,5,454,5,46,56,56,56,5,65,
#         6,54,5,54,6,54654654,1,456,5434,5,345,5,]
# ------------------------
# برنامه ای که بتواند در دیکشنری چیزی اضافه کند تغییر دهد یا نمایش دهد
# trans_dic={
#     "one":1,
#     "two":2,
#     "three":3,
#     "four":"4",
#     "hello":"salam"
# }
# ask=""
# while ask!="end":
#     ask=input("Choose one: view, add, edit or end : ")
#     if ask=="view":
#         for i in trans_dic:
#             print(i,"=",trans_dic[i])
#         #print(trans_dic)
#     elif ask=="add":
#         new_word=input("what do you want to add:")
#         new_word_meaning=input("what does it mean? ")
#         trans_dic[new_word]=new_word_meaning
#         print(trans_dic)
#     elif ask=="edit":
#         edit_word=input("which word do you want to edit:")
#         edit_word_meaning=input("what does it mean? ")
#         trans_dic[edit_word]=edit_word_meaning
#         print(trans_dic)
#     else:
#         print("you choose nothing! try again later!!!")
# ------------------------
# import json
# a={
#     "one":1,
#     "two":2,
#     "three":3,
#     "four":4
# }

# all_data=json.dumps(a)
# poul=open('moji.json',"w")
# poul.write(all_data)
# ----------------
# turtle.bgpic("anchor.png")
# turtle.write("you do it")
# turtle.penup()
# turtle.goto(0,-20)
# turtle.pendown()
# turtle.write("yes yes yes")
# turtle.done()
# -----------------------
# my_dic={
#     "m":'''                           
#           ____   
#         ,'  , `. 
#      ,-+-,.' _ | 
#   ,-+-. ;   , || 
#  ,--.'|'   |  || 
# |   |  ,', |  |, 
# |   | /  | |--'  
# |   : |  | ,     
# |   : |  |/      
# |   | |`-'       
# |   ;/           
# '---'            
# ''',

# }
# print(my_dic["m"])
# def a():
#     return 5,10
# print(a())
# -------------------
# To_Do_list=[1,2,3,"a",4,5,6]
# Time_List=[22,1,11,5,45,12,65]
# Delete_item=input("Enter Item to delete: ")
# if Delete_item in To_Do_list:
#     print("hey")
#     for j in range(len(To_Do_list)):
#         if Delete_item==To_Do_list[j]:
#             print("inja")
#             To_Do_list.pop(j)
#             print("ssss")
#             Time_List.pop(j)
#             print(333)
#             break
# print(To_Do_list)
# print(Time_List)
# ----------------------
# lis=["aaa","b","cc"]
# print(lis)
# name=input("enter a item")
# lis.remove(name)
# print(lis)
# ----------
lis=["aaa","b","cc"]
print(lis)
name=input("enter a item")
del lis[1]
print(lis)