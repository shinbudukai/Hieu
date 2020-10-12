import turtle
import random
#screen
rd_y= random.randint(-450,450)
rd_x = random.randint(-450,450)

#set up screen
wd = turtle.Screen()
wd.bgcolor("black")
wd.screensize(1280,720)


#set up border:
   
border = turtle.Turtle()
border.pendown()
border.pensize(10)
border.speed(0)
border.setpos(-450,-450)
border.color("white")
for side in range(4):
    border.fd(900)
    border.lt(90)
# road
'''
def road1(xcor,):
    road = turtle.Turtle()
    road.ht()
    road.pencolor("white")
    road.speed(0)
    road.penup()
    road.setpos(xcor,400)
    road.pensize(5)
    for i in range(30):
        road.seth(270)
        road.pendown()
        road.fd(30)
        road.penup()
        road.fd(30)
        road.pendown()
Allroads = road1(-225),road1(0),road1(225)
'''


All_road = []


def road(xcor):
    global roads
    global first_posy
    roads = []
    first_posy = 450
    for i in range(9):
        r = roads.append(turtle.Turtle())
    # roads in column
    for road in roads:
        road.shape("square")
        road.color("white")
        road.penup()
        road.ht()
        road.speed(0)
        road.goto(xcor,first_posy)
        first_posy -= 100
        road.st()
        
road(-225)
road(0)
roadspeed = 20
#main game loop

while True:
    for roads in All_road:
        road_y= roads.ycor()
        road_y -= roadspeed
        roads.sety(road_y)
        if roads.ycor() <= -300:
            roadspeed *= -1

        




