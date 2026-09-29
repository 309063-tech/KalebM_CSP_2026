import math
import turtle as trtl

sizes = {"small": 0.6, "medium": 0.9, "large": 1.1}
seal_size = input("Do you want your seal to be small, medium, or large? ").lower()

if seal_size not in sizes:
    print("Invalid input. Please choose small, medium, or large.")
    exit()

scale = sizes[seal_size]
appendage_scale = scale
import random

seal_color = random.choice(["gray", "lightgray", "white"])


screen = trtl.Screen()
seal = trtl.Turtle()
seal.speed(0)
seal.hideturtle()
seal.penup()

# body: oval
# head: separate oval attached to body

def draw_ellipse(center_x, center_y, width, height, color):
    seal.fillcolor(color)
    seal.pencolor("dimgray")
    seal.pensize(2)
    seal.begin_fill()
    seal.penup()
    seal.goto(center_x + width / 2, center_y)
    seal.pendown()
    for angle in range(0, 361, 5):
        rad = math.radians(angle)
        x = center_x + (width / 2) * math.cos(rad)
        y = center_y + (height / 2) * math.sin(rad)
        seal.goto(x, y)
    seal.end_fill()
    seal.penup()

# body uses user's size choice
body = (0, -20 * scale, 220 * scale, 150 * scale)
# head and appendages stay visible at small size but still move with the chosen size
head_center = (80 * appendage_scale, 18 * appendage_scale)
head_radius = 48 * appendage_scale
flipper_forward = 15 * appendage_scale

# flippers and tail scale with size change
left_flipper_top = [
    (-62 * appendage_scale + flipper_forward, 18 * appendage_scale),
    (-5 * appendage_scale + flipper_forward, 105 * appendage_scale),
    (38 * appendage_scale + flipper_forward, 88 * appendage_scale),
    (30 * appendage_scale + flipper_forward, 35 * appendage_scale),
    (-82 * appendage_scale + flipper_forward, 0 * appendage_scale),
]

left_flipper_bottom = [
    (-62 * appendage_scale + flipper_forward, -45 * appendage_scale),
    (-5 * appendage_scale + flipper_forward, -145 * appendage_scale),
    (38 * appendage_scale + flipper_forward, -115 * appendage_scale),
    (30 * appendage_scale + flipper_forward, -62 * appendage_scale),
    (-82 * appendage_scale + flipper_forward, -28 * appendage_scale),
]

tail = [
    (-72 * appendage_scale, -28 * appendage_scale),
    (-160 * appendage_scale, 8 * appendage_scale),
    (-140 * appendage_scale, -38 * appendage_scale),
    (-160 * appendage_scale, -75 * appendage_scale),
    (-62 * appendage_scale, -58 * appendage_scale),
]


def draw_polygon(points, color):
    seal.fillcolor(color)
    seal.pencolor("dimgray")
    seal.pensize(2)
    seal.begin_fill()
    seal.penup()
    seal.goto(points[0][0], points[0][1])
    seal.pendown()
    for x, y in points[1:]:
        seal.goto(x, y)
    seal.goto(points[0][0], points[0][1])
    seal.end_fill()
    seal.penup()

# draw flippers and tail first so the body covers their attachment edges
for points in [left_flipper_top, left_flipper_bottom, tail]:
    draw_polygon(points, seal_color)

# draw the body and keep its oval dimensions exact
cx, cy, w, h = body
draw_ellipse(cx, cy, w, h, seal_color)

# Fill the head over the body first, then draw only its circular outline.
seal.penup()
seal.goto(head_center)
seal.dot(2 * head_radius, seal_color)
seal.pencolor("dimgray")
seal.pensize(2)
seal.setheading(0)
seal.goto(head_center[0], head_center[1] - head_radius)
seal.pendown()
seal.circle(head_radius)
seal.penup()

screen.exitonclick()
