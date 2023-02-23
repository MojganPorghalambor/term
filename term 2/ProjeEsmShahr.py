import string
import os
import random
import time 
os.system("cls")
#----------------- start value -----------------
alphabet=list(string.ascii_lowercase)
case=random.choice(alphabet)
score1=0
score2=0
i=5

#----------------- timer -----------------
os.system("cls")
for i in range(5,0,-1):
    print(f"game is starting in {i}")
    time.sleep(1)
    os.system("cls")

#----------------- player1 -----------------
print("---------- player1 ----------")
name1=input(f"Enter a name with {case} : ")
city1=input(f"Enter a city with {case} : ")
os.system("cls")

#----------------- player2 -----------------
print("---------- player2 ----------")
name2=input(f"Enter a name with {case} : ")
city2=input(f"Enter a city with {case} : ")
os.system("cls")

#----------------- score for name -----------------
if len(name1)>2 and name1[0]==case:
    score1+=20
if len(name2)>2 and name2[0]==case:
    score2+=20
if name1==name2:
    score1-=10
    score2-=10

#----------------- score for city -----------------
if len(city1)>2 and city1[0]==case:
    score1+=20
if len(city2)>2 and city2[0]==case:
    score2+=20
if city1==city2:
    score1-=10
    score2-=10

#----------------- winning plan -----------------
if score1>score2:
    print("player 1 win")
elif score2>score1:
    print("player 2 win")
else:
    print("there is no winner")

print(f"player wrote name: {name1} and city: {city1}")
print(f"player wrote name: {name2} and city: {city2}")