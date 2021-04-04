import turtle
s = turtle.getscreen()

t = turtle.Turtle()

t.fillcolor("red")
t.pensize(3)
t.pencolor("blue")
t.begin_fill()

for i in range(360):
    t.forward(1)
    t.right(1)

t.end_fill()
