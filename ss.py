import turtle
import random
import time

delay=0.1
score=0
highestscore=0
#snake bodies
bodies=[]

# Geeting a screen
s=turtle.screen()
s.title("Snake Game")
s.bgcolor('gray')
s.setup(width=600,height=600)

#create Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color('white')
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('yellow')
food.fillcolor('green')
food.penup()
food.ht()
food.goto(0,200)
food.st()

#score board
sb=turtle.Turtle()
sb.shape('square')
sb.fillcolor('black')
sb.penup()
sb.goto(-250,-250)
sb.write('score:0 | Heighest Score:0')

def moveup():
    if head .direction !='down':
      head.direction ='up'
def movedown ():
    if head.direction!='up':
        head.direction='down'
def moveleft():
    if head.direction!='right':
        head.direction='left'
def moveright():
    if head.direction!='left':
        head.direction='right'
def movestop():
    head.direction='stop'
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction =='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.ycor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.ycor()
        head.setx(x+20)

# Event Handling -key mappings
s.listen()
s.onkey(moveup,'up')
s.onkey(movedown,'down')
s.onkey(moveleft,'left')
s.onkey(moveright,'right')
s.onkey(movestop,'space')

#main loop
while True:
    s.update()#this is to update the screen
    # check collison with border
    
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()>290:
        head.setx(-290)
    if head.ycor()<-290:
        head.sety(290)
    if head.ycor()<-290:
        head.sety(290)

#check collison with food
    if head.distance(food)<20:
     #move the food to new random place
     x=random.randint(-290,290)
     y=random.randint(-290,290)
     food.goto(x,y)
    #increase the length of the body
    body=turtle.Turtle()
    body.speed(0)
    body.penup()
    body.shape('square')
    body.color('red')
    body.fillcolor('black')
    body.append(body)#append new body
     
    #increase the score 
    score=score+10
    #change delay
    delay-=0.001
    #update the highest score
    if score>heighestscore:
        heighestscore=score
    sb.clear()
    sb.write( 'score:{} Highest Score:{}')



    #collison with snake body


    # check collison with food
    #check collison with snake body