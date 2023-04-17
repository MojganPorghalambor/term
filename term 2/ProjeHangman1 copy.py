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
man=1
checker=0
for i in range(len(word)):
    while len(guess)>1:
        print("just enter a character!")
        guess=input("Enter your guess:")
    for j in range(len(word)):
        if guess==word[j]:
            show[j]=guess
            checker=1
            # print("alaki")
            # print(word[i])
    if checker==0:
        print(manDic[man])
        man+=1
    checker=0
    if man==6:
        break
    print(show)
    print(f"lets have your {i+1} chance")        
    guess=input("Enter your guess:")

print("your time is over!")
if show==word:
    print("you wooooooooooooon!")
else:
    print("you loose!")

