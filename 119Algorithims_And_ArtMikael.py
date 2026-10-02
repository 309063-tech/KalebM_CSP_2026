import turtle as trtl

seal_size = trtl.textinput("Size" , "Do you want your seal to be small, medium, or large? ")
size = {"small": 0.6, "medium": 0.9, "large": 1.1}

if seal_size not in size:
    seal_size = trtl.textinput("Size", "Invalid input. Please type small, medium, or large: ")

if seal_size not in size:
    seal_size = trtl.textinput("Size", "Last chance. Type only small, medium, or large: ")

if seal_size not in size:
    print("Invalid input. Using medium by default.")
    seal_size = "medium"

scale = size[seal_size]
import random

seal_colors = ["gray", "lightgray", "darkgray"]
seal_color = random.choice(seal_colors)

screen = trtl.Screen()
seal = trtl.Turtle()
seal.speed(0)
seal.hideturtle()
seal.penup()

# body
seal.fillcolor(seal_color)
seal.begin_fill()
seal.showturtle()
seal.pendown()
seal.setheading(-60)
seal.goto(0, 0 * scale)
seal.left(90)
seal.circle(80 * scale, 180, 50)
seal.forward(30 * scale)
seal.right(360)
seal.circle(80 * scale, 180, 50)
seal.forward(30 * scale)
seal.end_fill()
seal.penup()

# head
seal.goto(38 * scale, 55 * scale)
seal.pendown()
seal.fillcolor(seal_color)
seal.begin_fill()
seal.circle(50 * scale)
seal.end_fill()
seal.penup()

# left flipper
seal.goto(-40 * scale, 120 * scale)
seal.pendown()
seal.fillcolor(seal_color)
seal.begin_fill()
seal.setheading(210)
seal.goto(-20 * scale, 190 * scale)
seal.goto(-75 * scale, 200 * scale)
seal.goto(-50 * scale, 120 * scale)
seal.goto(-40 * scale, 120 * scale)
seal.end_fill()
seal.penup()

# right flipper
seal.goto(50 * scale, -5 * scale)
seal.pendown()
seal.fillcolor(seal_color)
seal.begin_fill()
seal.setheading(210)
seal.goto(0 * scale, 30 * scale)
seal.goto(-10 * scale, 30 * scale)
seal.goto(5 * scale, -40 * scale)
seal.goto(50 * scale, -5 * scale)
seal.end_fill()
seal.penup()

# eyes
seal.goto(35 * scale, 120 * scale)
seal.pencolor("black")
seal.pendown()
seal.circle(10 * scale)
seal.penup()
seal.goto(0 * scale, 120 * scale)
seal.pencolor("black")
seal.pendown()
seal.circle(10 * scale)
seal.penup()

# whiskers
whisker_input = trtl.textinput("whiskers" , "How many whiskers do you want?(2-8) ")
whiskers = int(whisker_input)

if whiskers < 2 or whiskers > 8:
    whisker_input = trtl.textinput("Whiskers", "Please type a number from 2 to 8: ")
    whiskers = int(whisker_input)

if whiskers < 2 or whiskers > 8:
    whiskers = 8
    print("Invalid input. Using 8 whiskers by default.")

seal.color("black")
whisker_length = 10 * scale
seal.pensize(1 * scale)
#Draw whiskers
n = 0
while (n < whiskers):
      seal.penup()
      seal.goto(20 * scale,75 * scale)
      seal.pendown()
      if n < whiskers / 2:
        seal.setheading(180 - (n * 20))
      else:
        seal.setheading((n - (whiskers / 2)) * 20)
      seal.forward(whisker_length)
      n = n + 1
whisker_side =  whiskers % 8

# tail
seal.pencolor("black")
seal.penup()
seal.goto(-140 * scale, 20 * scale)
seal.pendown()
seal.fillcolor(seal_color)
seal.begin_fill()
seal.goto(-170 * scale, 45 * scale)
seal.goto(-150 * scale, -10 * scale)
seal.goto(-140 * scale, 20 * scale)
seal.end_fill()
seal.penup()

# Make spots

spot = (10 * scale, 0 * scale), (9 * scale, 2 * scale), (7 * scale, 4 * scale), (4 * scale, 5 * scale), (0 * scale, 5 * scale), (-4 * scale, 5 * scale), (-7 * scale, 4 * scale), (-9 * scale, 2 * scale),(-10 * scale, 0 * scale), (-9 * scale, -2 * scale), (-7 * scale, -4 * scale), (-4 * scale, -5 * scale), (0 * scale, -5 * scale), (4 * scale, -5 * scale), (7 * scale, -4 * scale), (9 * scale, -2 * scale)
screen.register_shape("my_spot", spot)
my_spot = trtl.Turtle(shape="my_spot")
my_spot.color("black")
my_spot.fillcolor("white")
my_spot.pendown()
my_spot.shapesize(1 * scale)
my_spot.penup()
my_spot.goto(-60 * scale, 20 * scale)
my_spot.left(90)
my_spot.stamp()
my_spot.goto(-100 * scale, 20 * scale )
my_spot.stamp()
my_spot.goto(-120 * scale, 40 * scale)
my_spot.stamp()
my_spot.goto(-80 * scale, 40 * scale )
my_spot.stamp()
my_spot.goto(-130 * scale, 60 * scale)
my_spot.stamp()
my_spot.goto(-90 * scale, 60 * scale)
my_spot.stamp()
my_spot.goto(-120 * scale, 80 * scale)
my_spot.stamp()
my_spot.goto(-80 * scale, 80 * scale)
my_spot.stamp()
my_spot.goto( -80 * scale, 0 * scale)
my_spot.stamp()
my_spot.goto(-40 * scale, 0 * scale)

screen.exitonclick()
screen.mainloop()
