import turtle  # allows for turtle graphics

t = turtle.Turtle()
t.speed(0)  # automatic speed


# movement functions (pen up, no line while moving)
def move_right():
    t.penup()
    t.setheading(0)  # East
    t.fd(100)


def move_up():
    t.penup()
    t.setheading(90)  # North
    t.fd(100)


def move_left():
    t.penup()
    t.setheading(180)  # West
    t.fd(100)


def move_down():
    t.penup()
    t.setheading(270)  # South
    t.fd(100)


# drawing functions (pen down, draw at current position)
def draw_square():
    t.pendown()
    t.color("black", "pink")
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.rt(90)
    t.end_fill()
    t.penup()


def draw_triangle():
    t.pendown()
    t.color("black", "forest green")
    t.begin_fill()
    for i in range(3):
        t.fd(70)
        t.lt(120)
    t.end_fill()
    t.penup()


def draw_circle():
    t.pendown()
    t.color("black", "red")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()


# screen + keyboard events
screen = turtle.Screen()
screen.title("Python Turtle Graphics")
screen.listen()

# arrow keys → move
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

# letter keys → draw shapes
screen.onkey(draw_square, "s")
screen.onkey(draw_triangle, "t")
screen.onkey(draw_circle, "c")

screen.mainloop()
