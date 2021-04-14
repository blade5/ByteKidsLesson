#-*-coding: utf-8-*-
import turtle
import time


def write(start, end):
    turtle.penup()
    turtle.setpos(start)
    turtle.pendown()
    turtle.goto(end)


def draw_little_heart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)


def draw_setup():
    #turtle.color('red', 'pink')
    turtle.pensize(15)
    #turtle.speed(2000)

    turtle.up()


def draw_left():
    turtle.hideturtle()
    turtle.color('red')
    turtle.goto(0,-180)
    turtle.showturtle()
    turtle.down()
    turtle.speed(2000)
    turtle.begin_fill()
    turtle.color('black')
    turtle.left(140)
    turtle.forward(224)
    draw_little_heart()


def draw_right():
    turtle.color('black')
    turtle.left(120)

    draw_little_heart()

    turtle.forward(224)
    turtle.end_fill()
    turtle.pensize(12)
    turtle.up()
    turtle.hideturtle()
    turtle.goto(0, -20)
    turtle.showturtle()


def draw_words():
    turtle.color('red')
    # sheng
    write((-150, 30), (-160, 10))
    write((-155, 20), (-105, 20))
    write((-150, -10), (-110, -10))
    write((-160, -40), (-100, -40))
    write((-130, 40), (-130, -40))

    # ri
    write((-75, 35), (-75, -35))
    write((-75, 35), (-20, 35))
    turtle.goto((-20,-35))
    write((-75, 0), (-20, 0))
    write((-75, -35), (-20, -35))


    # kuai
    write((30, 30), (20, 0))
    write((30, 30), (40, 0))
    write((30, 40), (30, -40))
    write((50, 20), (80, 20))
    turtle.goto((80, 0))
    write((35, 0), (100, 0))
    write((65, 40), (65, 0))
    turtle.goto((40, -40))
    write((65, 40), (65, 0))
    write((65, 0), (80, -40))

    # le
    write((160, 40), (110, 30))
    turtle.goto((110, 10))
    turtle.goto((170, 10))
    write((140, 35), (140, -40))
    turtle.goto((130, -30))
    write((120, -10), (110, -30))
    write((160, -10), (170, -30))
    turtle.up()


def draw_person(person):
    turtle.hideturtle()
    turtle.color('red')
    time.sleep(1)
    turtle.goto(180, -180)
    turtle.showturtle()
    turtle.write(person, font=(20, 25), align="right", move=True)


person = input('送给谁: ')


draw_setup()
draw_left()
draw_right()
draw_words()
draw_person(person)

window = turtle.Screen()
window.exitonclick()
