import turtle as trtl
import random as rand
#---------Start Screen Setup----------
turtle = trtl.Turtle()
turtle.pensize(2)
turtle.color("black")
turtle.penup()
turtle.goto(0, 150)
turtle.write("Select a Difficulty", align="center", font=("Arial", 40, "normal"))
turtle.goto(-75, 50)
turtle.pendown()
def create_button():
  turtle.pencolor("black")
  turtle.begin_fill()
  turtle.setheading(0)
  turtle.fillcolor("black")
  turtle.forward(150)
  turtle.left(90)
  turtle.forward(75)
  turtle.left(90)
  turtle.forward(150)
  turtle.left(90)
  turtle.forward(75)
  turtle.end_fill()
create_button()
turtle.goto(-25, 70)
turtle.color ("white")
turtle.write("Easy", font=("Arial", 20, "normal"))
turtle.penup()
turtle.goto(-75, -60)
turtle.pendown()
create_button()
turtle.goto(-50, -40)
turtle.color("white")
turtle.write("Medium", font=("Arial", 20, "normal"))
turtle.penup()
turtle.goto(-75, -180)
turtle.pendown()
create_button()
turtle.goto(-25, -160)
turtle.color("white")
turtle.write("Hard", font=("Arial", 20, "normal"))
turtle.hideturtle()

    








wn = trtl.Screen()
wn.mainloop()