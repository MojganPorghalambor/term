from random import choice
import os
import time
stuffList=["rock","paper","scissors"]
playerChoose=input("choose one : rock, paper, scissors: ")

playerScore=0
pcScore=0
while playerChoose !="end":
    while playerChoose!="rock" and playerChoose!="paper" and playerChoose!="scissors":
        playerChoose=input("choose one : rock, paper, scissors: ")
        if playerChoose=="end":
            break
    if playerChoose=="end":
        break
    pcChoose=choice(stuffList)
    print(f"I choose {pcChoose}")
    if playerChoose=="rock" and pcChoose=="scissors":
        playerScore+=1
        print("you win just this time!")
    elif playerChoose=="paper" and pcChoose=="rock":
        playerScore+=1
        print("you win just this time!")
    elif playerChoose=="scissors" and pcChoose=="paper":
        playerScore+=1
        print("you win just this time!")
    elif pcChoose=="rock" and playerChoose=="scissors":
        pcScore+=1
        print("I win hahaha")
    elif pcChoose=="paper" and playerChoose=="rock":
        pcScore+=1
        print("I win hahaha")
    elif pcChoose=="scissors" and playerChoose=="paper":
        pcScore+=1
        print("I win hahaha")
    else:
        print("equal for now!")
    time.sleep(2)    
    for i in range(5,0,-1):
        print(f"try again in {i}")
        time.sleep(1)
        os.system("cls")
    
    print(f"PC Score {pcScore}       Player Score {playerScore}")
    playerChoose=input("choose one : rock, paper, scissors: ")
    

