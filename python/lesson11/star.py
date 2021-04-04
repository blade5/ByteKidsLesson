import turtle
s = turtle.getscreen()
t = turtle.Turtle()

t.pencolor("red")
t.pensize(3)
t.fillcolor("yellow")
t.begin_fill()

for i in range(5):
    t.forward(100)

    t.right(180 - 36)

t.end_fill()
