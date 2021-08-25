import turtle
#键盘控制海龟移动
t=turtle.Pen() #设置一个海龟
s=turtle.Pen() #设置一条蛇
t.shape('turtle') #把海龟画笔造型改为‘海龟’
#设定初始位置
t.penup()
t.goto(200,200)
#限定海龟的移动范围，xcor获取画笔的x坐标，ycor获取画笔的y坐标，为了不使代码重复，我们使用一个函数来解决问题
def checkbound(z):
    if(z.xcor()>200):
        z.goto(200,z.ycor())
    if(z.xcor()<-200):
        z.goto(-200,z.ycor())
    if(z.ycor()>200):
        z.goto(z.xcor(),200)
    if(z.ycor()<-200):
        z.goto(z.xcor(),-200)
#键盘上下左右键位绑定函数，控制海龟的移动
screen=turtle.Screen()
def up():
    checkbound(t) #调用函数防止海龟超出范围
    t.setheading(90)
    t.forward(30)
def down():
    checkbound(t)
    t.setheading(270)
    t.forward(30)
def left():
    checkbound(t)
    t.setheading(180)
    t.forward(30)
def right():
    checkbound(t)
    t.setheading(0)
    t.forward(30)
#设置蛇追踪海龟
while True:
    screen.onkey(up,'Up')
    screen.onkey(down,'Down')
    screen.onkey(left,'Left')
    screen.onkey(right,'Right')
    #设置画布监听键盘事件开始
    screen.listen()
    s.speed(5)
#towards方法可以获取两只画笔直线的坐标方位角，setheading方法是朝坐标方位角改变方向，以x正轴为默认初始方向
#distance方法可以获取两只画笔之间的直线距离
#当蛇和海龟的距离小于30时，循环结束
    s.setheading(s.towards(t))
    s.forward(10)
    if(s.distance(t)<=30):
        turtle.write('游戏结束，蛇赢了')
        break
#设置不让画布关闭
screen.mainloop()
