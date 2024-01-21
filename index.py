import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
screen = turtle.Screen()
t.pensize(4)
radius = 200
number_of_teeth = 10
band_width = 10

def color_filled_circle(radius):
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def cog_teeth():
    for j in range(number_of_teeth):
        t.begin_fill()
        for i in range(2):
            t.left(90)
            t.forward(0.4 * radius)
            t.left(90)
            t.forward(0.35 * radius)
        t.end_fill()
        for i in range(2):
            t.left(90)
            t.forward(band_width)
        t.fillcolor("black")
        t.begin_fill()
        for i in range(2):
            t.forward(0.25 * radius)
            t.right(90)
            t.forward(0.3 * radius)
            t.right(90)
        t.end_fill()
        t.penup()
        t.home()
        t.left((360 / number_of_teeth) * (1 + j))
        t.forward(1.2 * radius)
        t.left(90)
        t.forward(0.175 * radius)
        t.color("green")
        t.pendown()

t.penup()
t.forward(radius)
t.left(90)
t.color("green")
t.pendown()
color_filled_circle(radius)
t.right(90)
t.penup()
t.forward(0.2 * radius)
t.left(90)
t.forward(0.175 * radius)
t.pendown()
cog_teeth()
t.penup()
radius = radius - band_width
t.goto(radius, 0)
t.color("black")
color_filled_circle(radius)
radius = 0.6 * radius
t.goto(radius, 0)
t.color("green")
color_filled_circle(radius)
radius = radius - 1.3 * band_width
t.goto(radius, 0)
t.color("black")
color_filled_circle(radius)
t.hideturtle()
screen.exitonclick()
