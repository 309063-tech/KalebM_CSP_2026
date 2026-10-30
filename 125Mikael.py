import turtle as trtl
import random as rand
import time 

#---------Start Screen Setup----------
turtle = trtl.Turtle()
wn = trtl.Screen()
wn.title("Target Practice")
turtle.pensize(2)
turtle.speed(0)
turtle.color("black")
turtle.penup()
turtle.goto(0, 150)
turtle.write("Select a Difficulty", align="center", font=("Arial", 40, "normal"))
turtle.goto(-75, 50)
turtle.pendown()


#--------Creating different difficulties------
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
turtle.goto(-30, 70)
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
turtle.goto(-75, -170)
turtle.pendown()
create_button()
turtle.goto(-30, -150)
turtle.color("white")
turtle.write("Hard", font=("Arial", 20, "normal"))
turtle.hideturtle()

counter = trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(175, 290)
font_setup = ("Arial", 30, "normal")
timer = 30
counter_interval = 1000   
timer_up = False

score = 0
score_display = trtl.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.goto(-320, 290)
font_setup = ("Arial", 30, "normal")
score_display.write("Score: " + str(score), font=font_setup)

difficulty = ""
target_x = 0
target_y = 0
target_checker = trtl.Turtle()
target_checker.hideturtle()
target_checker.penup()
#-----Making functions----
def check_click(x, y):
  global difficulty
  if -75 <= x <= 75 and 50 <= y <= 125:
    difficulty = "Easy"
  elif -75 <= x <= 75 and -60 <= y <= 15:
    difficulty = "Medium"
  elif -75 <= x <= 75 and -170 <= y <= -95:
    difficulty = "Hard"
  else:
    return
  
  turtle.clear()
  turtle.penup()
  turtle.goto(0, 0)
  turtle.color("black")
  turtle.write("Difficulty: " + difficulty, align="center", font=font_setup)
  wn.onclick(None)
  wn.ontimer(start_game, 1000)

def start_game():
  create_target()
  wn.onclick(check_target)
  countdown()

def create_target():
  global target_x, target_y
  turtle.clear()
  target_x = rand.randint(-200, 200)
  target_y = rand.randint(-100, 100)
  target_checker.goto(target_x, target_y)
  if difficulty == ("Easy"):
    for radius, color in [(90, "blue"), (60, "red"), (30, "yellow")]:
      turtle.penup()
      turtle.goto(target_x, target_y - radius)
      turtle.setheading(0)
      turtle.color(color)
      turtle.pendown()
      turtle.begin_fill()
      turtle.circle(radius)
      turtle.end_fill()
  elif difficulty == ("Medium"):
    for radius, color in [(75, "blue"), (50, "red"), (25, "yellow")]:
      turtle.penup()
      turtle.goto(target_x, target_y - radius)
      turtle.setheading(0)
      turtle.color(color)
      turtle.pendown()
      turtle.begin_fill()
      turtle.circle(radius)
      turtle.end_fill()
  elif difficulty == ("Hard"):
    for radius, color in [(60, "blue"), (40, "red"), (20, "yellow")]:
      turtle.penup()
      turtle.goto(target_x, target_y - radius)
      turtle.setheading(0)
      turtle.color(color)
      turtle.pendown()
      turtle.begin_fill()
      turtle.circle(radius)
      turtle.end_fill()
  turtle.penup()


if difficulty == "Easy":
 center_radius = 30
 middle_radius = 60
 outer_radius = 90
if difficulty == "Medium":
 center_radius = 25
 middle_radius = 50
 outer_radius = 75
if difficulty == "Hard":
 center_radius = 20
 middle_radius = 40
 outer_radius = 60
def check_target(x, y):
  global score
  if timer_up:
    return
  distance = target_checker.distance(x, y)
  if distance <= 30:
    print("You gained 100 points")
    score +=100
    update_score()
    turtle.clear()
    create_target()
  elif distance <= 60:
    print("You gained 50 points")
    score +=50
    update_score()
    turtle.clear()
    create_target()
  elif distance <= 90:
    print("You gained 25 points")
    score +=25
    update_score()
    turtle.clear()
    create_target()
  else:
     print("Miss")
     if difficulty == "Medium" or difficulty == "Hard":
      timer -= 1
      counter.clear()
      counter.write("Timer: " + str(timer), font=font_setup)

def update_score():
  score_display.clear()
  score_display.write("Score: " + str(score), font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    wn.onclick(None)

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 








wn.onclick(check_click)
wn.mainloop()
