import turtle
import math

# Set the background color
screen = turtle.Screen()
m = turtle.Turtle()
screen.bgcolor("skyblue")

def drawSun( x, y, size):
 m.setheading(0)
 m.fillcolor("yellow")
 m.penup()
 m.goto(x, y)
 m.pendown()
 m.begin_fill()
 m.pencolor('yellow')
 m.pensize(10)
 m.circle(size)
 m.end_fill()
drawSun(-400,220,50)
# Create our turtle
george = turtle.Turtle()
george.color("black")
george.speed(10)


t = turtle.Pen()


pen = turtle.Turtle()
# 3. Set up your turtle
pen.speed(0)
def drawCloud(pen, x, y):
    pen.setheading(90)
    pen.fillcolor("white")
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()

    pen.color("white")
    for x in range(15):
        pen.circle(30)
        pen.right(36)
        pen.forward(10)
    pen.end_fill()
    pen.setheading(90)
drawCloud(pen,270,80)
drawCloud(pen,-270,80)
t.pensize(10)
t.pencolor('black')
t.speed(0)
t.penup()
t.goto(-220,120)
t.pendown()
def mm(c):
    t.left(90)
    t.begin_fill()

    for x in range(180):
        t.color(c)
        t.forward(4)
        t.right(1)
    t.right(90)
    t.forward(460)
    t.end_fill()


mm('red')
t.penup()
t.right(90)
t.goto(-220,90)
t.pendown()
t.begin_fill()
for x in range(180):
    t.fillcolor('yellow')
    t.color('yellow')
    t.forward(4)
    t.right(1)
t.right(90)
t.forward(460)
t.end_fill()

t.penup()
t.right(90)
t.goto(-220,50)
t.pendown()
t.begin_fill()
for x in range(180):
    t.fillcolor('lightgreen')
    t.color('lightgreen')
    t.forward(4)
    t.right(1)
t.right(90)
t.forward(460)
t.end_fill()

t.penup()
t.right(90)
t.goto(-160,40)
t.pendown()
t.begin_fill()
for x in range(180):

    t.color('skyblue')
    t.forward(3)
    t.right(1)
t.right(90)
t.forward(260)
t.end_fill()



pen1 = turtle.Turtle()
# 3. Set up your turtle
pen1.speed(100)
def drawGrass(pen1):
  pen1.setheading(90)
  pen1.fillcolor('green')
  pen1.penup()
  pen1.setheading(90)
  pen1.goto(-800,-350)
  pen1.begin_fill()

  for x in range(2):
    pen1.forward(320)
    pen1.right(90)
    pen1.forward(1800)
    pen1.right(90)
  pen1.end_fill()
drawGrass(pen1)
def drawPath(pen1):
  pen1.setheading(90)
  pen1.color('black')
  pen1.fillcolor('#B87333')
  pen1.penup()
  pen1.goto(-155,-295)
  pen1.begin_fill()
  pen1.pendown()
  pen1.right(10)
  pen1.forward(203)
  pen1.right(80)
  pen1.forward(40)
  pen1.right(80)
  pen1.forward(203)
  pen1.right(80)
  pen1.end_fill()
  pen1.setheading(90)
drawPath(pen1)

def drawFence(pen1):
  pen1.setheading(90)
  pen1.color('black')
  #fence
  pen1.penup()
  pen1.goto(-679,-300)
  pen1.pendown()
  pen1.setheading(90)

  #pen.left(50)
  pen1.fillcolor("#7B3F00")
  pen1.begin_fill()
  for x in range(43):
    pen1.forward(100)
    pen1.right(45)
    pen1.forward(20)
    pen1.right(90)
    pen1.forward(20)
    pen1.right(45)
    pen1.forward(100)
    pen1.left(90)
    pen1.forward(4)
    pen1.left(90)
  pen1.end_fill()

  #handle
  pen1.penup()
  pen1.goto(-70,-250)
  pen1.pendown()
  pen1.fillcolor("#7B3F00")
  pen1.begin_fill()
  pen1.circle(7)
  pen1.end_fill()
  pen1.begin_fill()
  pen1.fillcolor("black")
  pen1.penup()
  pen1.goto(-74,-250)
  pen1.pendown()
  pen1.circle(4)
  pen1.end_fill()

  #hinges
  coord1 = [-145,-290]
  coord2 = [-145,-230]
  l = [coord1,coord2]
  for y in range(2):
    pen1.penup()
    pen1.goto(l[y])
    pen1.fillcolor("black")
    pen1.begin_fill()
    pen1.pendown()
    for x in range (2):
      pen1.forward(10)
      pen1.right(90)
      pen1.forward(15)
      pen1.right(90)
    pen1.end_fill()
  pen1.setheading(90)
drawFence(pen1)
# Define a funtion to draw and fill a rectangle with the given
# dimensions and color
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


# Define a function to draw and fill an equalateral right
# triangle with the given hypotenuse length and color.  This
# is used to create a roof shape.
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()


# Define a function to draw and fill a parallelogram, used to
# draw the side of the house
def drawParallelogram(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(90)
    t.end_fill()


# Define a function to draw four sun rays of the given length,
# for the sun of the given radius.  The turtle starts in the
# center of the circle.
def drawFourRays(t, length, radius):
    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + radius)
        t.left(90)


# Draw and fill the front of the house
george.penup()
george.goto(-150, -120)
george.pendown()
drawRectangle(george, 200, 110, "white")

# Draw and fill the front door
george.penup()
george.goto(-120, -120)
george.pendown()
drawRectangle(george, 40, 60, "lightgreen")

# Front roof
george.penup()
george.goto(-150, -10)
george.pendown()
drawTriangle(george, 200, "#FF9966")

# Side of the house
george.penup()
george.goto(50, -120)
george.pendown()
drawParallelogram(george, 110, 110, "white")

# Window
george.penup()
george.goto(70, -70)
george.pendown()
drawParallelogram(george, 30, 30, "lightblue")

# Side roof

# handle
pen.fillcolor("yellow")
pen.penup()
pen.goto(-100,-110 + 20)
pen.begin_fill()
pen.circle(4)
pen.end_fill()
george.penup()
george.goto(-50, 90)
george.pendown()
george.fillcolor("skyblue")
george.begin_fill()
george.left(30)
george.forward(120)
george.right(80)
george.forward(110 / math.sqrt(2))
george.forward(61)
george.right(90)

george.end_fill()

def drawTriangle(t, length, color):

    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()
m.penup()
m.pensize(2)
m.goto(-600,-150)
m.pendown()
def car():
 m.pencolor("darkred")
 m.color("darkred")
 m.begin_fill()

 m.forward(370)
 m.left(90)
 m.forward(50)
 m.left(90)
 m.forward(370)
 m.left(90)
 m.forward(50)
 m.end_fill()
 m.backward(50)
 m.left(90)
 m.forward(110)
 m.left(45)
 m.forward(72)
 m.right(45)
 m.forward(80)
 m.right(45)
 m.forward(72)
 m.right(135)
 m.forward(85)
 m.right(90)
 m.forward(50)
 m.penup()
 m.goto(-300,-150)
 m.pendown()
 m.color("black")
 m.begin_fill()
 m.circle(20)
 m.end_fill()
 m.penup()
 m.goto(-500, -150)
 m.pendown()
 m.color("black")
 m.begin_fill()
 m.circle(20)
 m.end_fill()
car()
def ballon():
 m.penup()
 m.goto(-400,0)
 m.pendown()
 m.color('red')
 m.begin_fill()
 m.circle(25)
 m.end_fill()
 m.pencolor('black')
 m.left(185)
 m.forward(100)
 m.pencolor('black')
 m.right(210)
 m.forward(100)
 m.color('#FF1493')
 m.begin_fill()
 m.circle(25)
 m.end_fill()
 m.penup()
 m.goto(-345,80)
 m.pendown()
 m.color('#BC8F8F')
 m.begin_fill()
 m.circle(25)
 m.end_fill()
 m.pencolor('black')
 m.right(170)
 m.forward(185)
 m.right(170)
 m.forward(150)
 m.color('darksalmon')
 m.begin_fill()
 m.circle(25)
 m.end_fill()
ballon()
m.hideturtle()

george.hideturtle()
m.hideturtle()
pen1.hideturtle()
pen.hideturtle()
turtle.done()