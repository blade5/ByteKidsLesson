import turtle

s = turtle.getscreen()
t = turtle.Turtle()


def write(start, end):
    t.penup()
    t.setpos(start)
    t.pendown()
    t.goto(end)


t.pensize(4)
t.pencolor("red")

# sheng
write((-150, 30), (-160, 10))
write((-155, 20), (-105, 20))
write((-150, -10), (-110, -10))
write((-160, -40), (-100, -40))
write((-130, 40), (-130, -40))

# ri
write((-75, 35), (-75, -35))
write((-75, 35), (-20, 35))
t.goto((-20,-35))
write((-75, 0), (-20, 0))
write((-75, -35), (-20, -35))


# kuai
write((30, 30), (20, 0))
write((30, 30), (40, 0))
write((30, 40), (30, -40))
write((50, 20), (80, 20))
t.goto((80, 0))
write((35, 0), (100, 0))
write((65, 40), (65, 0))
t.goto((40, -40))
write((65, 40), (65, 0))
write((65, 0), (80, -40))

# le
write((160, 40), (110, 30))
t.goto((110, 10))
t.goto((170, 10))
write((140, 35), (140, -40))
t.goto((130, -30))
write((120, -10), (110, -30))
write((160, -10), (170, -30))


t.hideturtle()

s.exitonclick()
