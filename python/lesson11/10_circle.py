import turtle
s = turtle.getscreen()

t = turtle.Turtle()

number = 10

for i in range(number):
    t.circle(100)

    t.right(360 / number)
