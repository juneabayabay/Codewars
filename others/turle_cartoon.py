import turtle

# Create the turtle screen and turtle
ts = turtle.getscreen()
t = turtle.Turtle()

# Set drawing speed
t.speed(5)

# -------------------------
# HEAD
# -------------------------
t.penup()
t.goto(0, -150)
t.pendown()

t.color("black", "lightyellow")
t.begin_fill()
t.circle(150)
t.end_fill()

# -------------------------
# LEFT EYE
# -------------------------
t.penup()
t.goto(-60, 40)
t.pendown()

t.color("black", "white")
t.begin_fill()
t.circle(30)
t.end_fill()

# Left pupil
t.penup()
t.goto(-60, 50)
t.pendown()

t.color("black")
t.begin_fill()
t.circle(12)
t.end_fill()

# -------------------------
# RIGHT EYE
# -------------------------
t.penup()
t.goto(60, 40)
t.pendown()

t.color("black", "white")
t.begin_fill()
t.circle(30)
t.end_fill()

# Right pupil
t.penup()
t.goto(60, 50)
t.pendown()

t.color("black")
t.begin_fill()
t.circle(12)
t.end_fill()

# -------------------------
# NOSE
# -------------------------
t.penup()
t.goto(0, 20)
t.pendown()

t.color("black", "orange")
t.begin_fill()

for i in range(3):
    t.forward(35)
    t.left(120)

t.end_fill()

# -------------------------
# MOUTH
# -------------------------
t.penup()
t.goto(-60, -40)
t.setheading(0)
t.pendown()

t.color("black", "red")
t.begin_fill()

# Draw a simple smile/mouth
t.forward(120)
t.right(90)
t.forward(50)
t.right(90)
t.forward(120)
t.right(90)
t.forward(50)

t.end_fill()

# -------------------------
# LEFT EAR
# -------------------------
t.penup()
t.goto(-140, 100)
t.pendown()

t.color("black", "pink")
t.begin_fill()
t.circle(45)
t.end_fill()

# -------------------------
# RIGHT EAR
# -------------------------
t.penup()
t.goto(140, 100)
t.pendown()

t.color("black", "pink")
t.begin_fill()
t.circle(45)
t.end_fill()

# -------------------------
# BODY
# -------------------------
t.penup()
t.goto(-100, -150)
t.setheading(0)
t.pendown()

t.color("black", "skyblue")
t.begin_fill()

for i in range(2):
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)

t.end_fill()

# -------------------------
# LEFT ARM
# -------------------------
t.penup()
t.goto(-100, -190)
t.setheading(180)
t.pendown()

t.color("black")
t.forward(80)

# -------------------------
# RIGHT ARM
# -------------------------
t.penup()
t.goto(100, -190)
t.setheading(0)
t.pendown()

t.forward(80)

# -------------------------
# FEET
# -------------------------
t.penup()
t.goto(-70, -300)
t.setheading(0)
t.pendown()

t.color("black", "green")
t.begin_fill()
t.circle(35)
t.end_fill()

t.penup()
t.goto(70, -300)
t.pendown()

t.color("black", "green")
t.begin_fill()
t.circle(35)
t.end_fill()

# Hide turtle
t.hideturtle()

# Keep the window open
turtle.done()