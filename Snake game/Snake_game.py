import turtle
import time
import random

delay=0.1
score=0
highscore=0
#Snake bodies
bodies=[]

#Getting a screen|Canvas
s=turtle.Screen()
s.title("Muzzammil snake game")
s.bgcolor("green")
s.setup(width=600,height=600)
 #Getting a snake
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.fillcolor("yellow")
head.penup()
head.goto(0,0)   #because it works in cordinate system (x,y)axis initially it is at center
head.direction="stop"

#Getting a snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("blue")
food.penup()
food.ht()
food.goto(0,200)    #It is basically the initial place of snake food
food.st()

#Getting a score board

sb=turtle.Turtle()
# sb.shape("circle")
sb.color("black")
sb.penup()
sb.goto(-250,-250)
sb.write("Score:0  | Highest score: 0")

#now defining  functions to move snake in all four directions
def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)                #This all is basically movement of snake head
    if head.direction=="left":        #Acording to coordinates 
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#Event handling It is basically that which judges the key pressed by the user
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveright,"Right")    #onkey is very useful function 
s.onkey(moveleft,"Left")      #whose index is s.onkey(functionname,key)
s.onkey(movestop,"space")


#mainloop
while True:
    s.update()  #This is to update the screen

#check collision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)    
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

#check collision with food
    if head.distance(food)<20:
        #move food on other place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

#increase the length of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)

#increase the score
        score=score+10
#change delay
        delay-=0.001
#highscore handling
        if score>highscore: 
            highscore=score
        sb.clear()
        sb.write("score:{} highscore:{}".format(score,highscore))  
#move the snake body
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
    
#check collisions with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
#hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1
            #update the scoreboard
            sb.clear()
            sb.write("score:{} Highscore:{}".format(score,highscore))
    time.sleep(delay)
s.mainloop()