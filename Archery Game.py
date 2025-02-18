# Archery board: 10 circles (1-10)
# Archery graphics
# Targeting arrow
# Scoreboard review: Set #: (points)

import turtle 
import random

wn = turtle.Screen()
wn.title("Archery Memo!")

# BOARD VARIABLES 
outer_xcoor = -200 
outer_fd = 400 
inner_xcoor = -185 
inner_fd = 370 
radius = 180

# BOARD SET-UP
romeo = turtle.Turtle()
romeo.shape("circle")
romeo.shapesize(0.7)
romeo.speed(10)
romeo.ht()
# Square board - outer
romeo.pu()
romeo.goto(-200, 205)
romeo.pd()
for i in range(4):
    romeo.fd(outer_fd)
    romeo.right(90)
    romeo.align="center"
# Square board - inner
romeo.pu()
romeo.goto(-185, 190)
romeo.pd()
romeo.fillcolor("saddlebrown")
for i in range(4):
    romeo.fd(inner_fd)
    romeo.right(90)
    romeo.stamp()

# Target - 10 rings
romeo.pu()
romeo.goto(0, -165)
romeo.pd()
ycoor = -175
num = 0

# CENTER SET-UP
point = turtle.Turtle()
point.ht()
point.pu()
point.goto(0, 16)

# Drawing circles based on radius
while radius >= 0:
    # Decrease the radius and increase
    # the vertical starting point to coordinate each radius at the center
    radius -= 15
    ycoor += 16
    num += 1
    # Every two circles go with a fill and outline color
    if radius >= 150:
        romeo.fillcolor("white")
        romeo.pencolor("black")
        romeo.begin_fill()
        romeo.pu()
        romeo.goto(0, ycoor)
        romeo.pd()
        romeo.circle(radius)
        romeo.end_fill()

    elif 120 <= radius < 150:
        romeo.fillcolor("black")
        romeo.pencolor("white")
        romeo.begin_fill()
        romeo.pu()
        romeo.goto(0, ycoor)
        romeo.pd()
        romeo.circle(radius)
        romeo.end_fill()

    elif 90 <= radius < 120:
        romeo.fillcolor("blue")
        romeo.pencolor("black")
        romeo.begin_fill()
        romeo.pu()
        romeo.goto(0, ycoor)
        romeo.pd()
        romeo.circle(radius)
        romeo.end_fill()

    elif 60 <= radius < 90:
        romeo.fillcolor("red")
        romeo.begin_fill()
        romeo.pu()
        romeo.goto(0, ycoor)
        romeo.pd()
        romeo.circle(radius)
        romeo.end_fill()

    elif 30 <= radius < 60:
        romeo.fillcolor("yellow")
        romeo.begin_fill()
        romeo.pu()
        romeo.goto(0, ycoor)
        romeo.pd()
        romeo.circle(radius)
        romeo.end_fill()
    
    # Labeling the score each circle coordinates
    romeo.ht()
    romeo.pu()
    romeo.goto(radius - 10.5, 5)
    romeo.pd()
    if num <= 9:
     romeo.write(f"{num}", font=("Monospace", 9, "bold"))

# 'SCORE' LABEL
pen_zero = turtle.Turtle()
pen_zero.ht()
pen_zero.pu()
pen_zero.goto(-65, 220)
pen_zero.write("Score: ", font=("Arial", 20, "bold"))

# BALL SET-UP
juliet = turtle.Turtle()
juliet.pu()
juliet.goto(0, 16)
juliet.shapesize(0.7)
juliet.speed(2)
juliet.color("darkgray", "lightgray")
juliet.shape("circle")

# SCORING SET-UP
score = 0
pen = turtle.Turtle()
pen.pu()
pen.ht()
pen.goto(25, 220)
pen.write(f"{score}", font=("Arial", 20, "italic"))

# ATTEMPT VARIABLE
attempt = 10

# Speed is how fast the ball moves around
juliet.speed(1.3)
# SCORING SET-UP
def scoring():
 # Globarize access to local variables attempt, score
 global attempt
 global score
 # Adding points based on distance with the center 
 # and subtracting 1 attempt every time the ball is clicked
 if point.distance(juliet) > 150 :
   score += 0
   attempt -= 1
 elif 135 <= point.distance(juliet) <= 150:
   score += 1
   attempt -= 1
 elif 120 <= point.distance(juliet) <= 135:
   score += 2
   attempt -= 1
 elif 105 <= point.distance(juliet) <= 120:
   score += 3
   attempt -= 1
 elif 90 <= point.distance(juliet) <= 105:
   score += 4
   attempt -= 1
 elif 75 <= point.distance(juliet) <= 90:
   score += 5
   attempt -= 1
 elif 60 <= point.distance(juliet) <= 75:
   score += 6
   attempt -= 1
 elif 45 <= point.distance(juliet) <= 60:
   score += 7
   attempt -= 1
 elif 30 <= point.distance(juliet) <= 45:
   score += 8
   attempt -= 1
 elif 15 <= point.distance(juliet) <= 30:
   score += 9
   attempt -= 1
 elif point.distance(juliet) <= 15:
   score += 10
   attempt -= 1
 
 # Erase the last score and show the new score after clicking
 pen.clear()
 pen.write(score, font=("Monospace", 20, "normal"))
 # Randomize the ball's location 
 for i in range(20):
  x = random.randint(-150, 150)
  y = random.randint(-150, 150)
  juliet.pu()
  juliet.goto(x, y)
  # Ending game when 10 attempts are reached by break the function
  if attempt == 0:
   pen_zero.clear()
   pen.clear()
   pen.goto(-80, 220)
   pen.write(f"Total: {score}/100", font=("Monospace", 20, "normal"))
   break
   

wn.listen()
wn.onkey(scoring, "Up")

wn.mainloop()
