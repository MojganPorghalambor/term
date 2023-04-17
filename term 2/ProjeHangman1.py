import random
import time
import os
from ProjeHangman2 import *
a = {
     "alaki":"!!!!!!!!!!!!!"
}
os.system("cls")
print("***Welcome to Hangman game***")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(1)
print("Let's play Hangman!")
time.sleep(3)
words= ["pizza","python","picture","film","poulstar","programming","game"]
word = random.choice(words)
wordlength = len(word)
show='_'*wordlength
show=list(show)
print(show)
print(type(show))

guess = print(f"This is the Hangman Word: {show}")
print("1 chance!")
guess=input("Enter your guess:")
chance=1
counter=1
fake_index = 0
for i in range(len(word)):
    while len(guess)>1:
        print("just enter a character!")
        guess=input("Enter your guess:")
    for j in word:
        if guess==j:
            print("you guess right!")
            show[fake_index]=guess
        fake_index+=1
    if guess not in word:
            print(manDic[counter])
            print(a["alaki"])
            counter+=1
            

    print(show)
    print(f"lets have your {i} chance")        
    if counter==6:
         break
    guess=input("Enter your guess:")
    fake_index=0
print("your time is over!")
if show==word:
    print("you wooooooooooooon!")
else:
    print("you loose!")
#m
