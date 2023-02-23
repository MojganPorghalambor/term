import turtle
import os
import random
from ProjeTurtleMatch2 import quastions

def GameScreen():
    s=turtle.Screen()
    s.bgcolor("red")
    s.title("2 player game")

def detail():
    colors=["blue","yellow","black","white"]
    tcolor=input("Enter a color: white, green, yellow, black, blue :")
    while True:
        if tcolor in colors:
            break
        tcolor=input("Enter a color: white, green, yellow, black, blue :")

    shapes=["arrow","turtle","circle" , "square" , "triangle" , "classic"]
    tshape=input("choose a shape: arrow, turtle, circle , square , triangle , classic :")
    while True:
        if tshape in shapes:
            break
        tshape=input("choose a shape: arrow, turtle, circle , square , triangle , classic :")

    return tcolor,tshape

def goal(player,x,y):
    player.goto(x,y)
    player.pendown()
    player.circle(40)
    player.penup()

def play():
    vasete=list(quastions.keys())
    entekhab=random.choice(vasete)
    print(entekhab)
    javab=int(input("enter your answer:"))
    if javab == quastions[entekhab]:
        print("good job")
        return 40
    else:
        print("wrong!")
        return 0

def draw(player,point):
    player.fd(point)


#---------main----------
os.system("cls")
#player1
GameScreen()
a,b=detail()
player1=turtle.Turtle()
player1.color(a)
player1.shape(b)
player1.penup()

#player2
a,b=detail()
player2=turtle.Turtle()
player2.color(a)
player2.shape(b)
player2.penup()

#draw circles
goal(player1,300,60)
goal(player2,300,-140)

#start position
player1.goto(-200,100)
player2.goto(-200,-100)

#start game
while True:
    print("player 1 :")
    point1=play()
    draw(player1,point1)
    print("player 2 :")
    point2=play()
    draw(player2,point2)
    if player1.pos()>= (250,100) and player2.pos()>=(250,-100):
        os.system("cls")
        print("you both try hard, so...")
        print("there is no winner!")
    if player1.pos()>= (250,100):
        os.system("cls")
        print("Player 1 win!")
        break
    elif player2.pos()>=(250,-100):
        os.system("cls")
        print("Player 2 win!")
        break
    
print("thank you for playing this game, see you soon :>")
turtle.done()
