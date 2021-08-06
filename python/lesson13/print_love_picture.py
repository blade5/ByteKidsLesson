import turtle
import time


def draw_setup():
    turtle.Screen().setup(width=900, height=600)
    turtle.color('red') # 设置颜色, 可以改成你喜欢的颜色
    turtle.pensize(15) # 设置笔墨的粗细
    turtle.speed(10)
    turtle.up()
    turtle.goto(0,-180)
    turtle.down()


def draw_little_heart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)


def draw_left():
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    draw_little_heart()


def draw_right():
    turtle.left(120)
    draw_little_heart()
    turtle.forward(224)
    turtle.end_fill()


def write(start, end):
    turtle.penup()
    turtle.setpos(start)
    turtle.pendown()
    turtle.goto(end)


def draw_words():
    turtle.pensize(15)
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
    write((-20, 35), (-20,-35))
    write((-75, 0), (-20, 0))
    write((-75, -35), (-20, -35))

    # kuai
    write((30, 30), (20, 0))
    write((30, 30), (40, 0))
    write((30, 40), (30, -40))
    write((50, 20), (80, 20))
    write((80, 20), (80, 0))
    write((35, 0), (100, 0))
    write((65, 40), (65, 0))
    write((65, 0), (40, -40))
    write((65, 40), (65, 0))
    write((65, 0), (80, -40))

    # le
    write((160, 40), (110, 30))
    write((110, 30), (110, 10))
    write((110, 10), (170, 10))
    write((140, 35), (140, -40))
    write((140, -40), (130, -30))
    write((120, -10), (110, -30))
    write((160, -10), (170, -30))
    turtle.up()

def draw_person(person):
    turtle.color('black') # 改一下颜色
    time.sleep(1)
    turtle.goto(180, -180)
    turtle.write(person, font=(20, 25), align="center", move=True)

draw_setup()
draw_left()
draw_right()
draw_words()

person = input('送给谁: ')
draw_person("person")
