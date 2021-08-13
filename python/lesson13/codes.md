```python
import turtle # 画图库
# 设置背景

bg = turtle.Screen() #得到屏幕对象bg
bg.bgcolor("black") #背景颜色

# Bottom Line 1
turtle.penup() #停止画笔
turtle.goto(-170,-180) #来到位置-170,-180
turtle.color("white") #设置颜色
turtle.pendown() #开始画笔
turtle.forward(350) #往前350px?

# Mid Line 2
turtle.penup() #停止画笔
turtle.goto(-160,-150) #来到位置-160,-150
turtle.color("white") #设置颜色
turtle.pendown() #开始画笔
turtle.forward(300) #往前300px

# Up Line 1
turtle.penup() #停止画笔
turtle.goto(-150,-120) #来到位置-150,-120
turtle.color("white") #设置颜色
turtle.pendown() #开始画笔
turtle.forward(250) #往前250px

turtle.penup() #停止画笔
turtle.goto(-100,-100) #来到位置-100,-100
turtle.color("white") #设置颜色 为白色

turtle.begin_fill() #开始填充颜色
turtle.pendown()  #开始画笔
turtle.forward(140) #向前移动 140px?
turtle.left(90) #向左转向90度
turtle.forward(95) #向前移动 95px?
turtle.left(90) #向左转向90度
turtle.forward(140) #向前移动 140px?
turtle.left(90) #向左转向90度
turtle.forward(95) #向前移动 95px?
turtle.end_fill()  #结束填充颜色

turtle.penup() #停止画笔
turtle.goto(-90,0) #来到位置 -90，0
turtle.color("red") #设置颜色红色
turtle.left(180) #左转180度 ->决定画笔前进的方向
turtle.pendown() #开始画笔
turtle.forward(20) #向前20px

turtle.goto(-90,0) #分别位置 -60，-30，0
turtle.color("red") #设置颜色红色

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"] #定义圆圈的颜色数组
turtle.penup() #抬起画笔
turtle.goto(-40,-50) #来到位置-40, -50
turtle.pendown() #放下画笔

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color) #设置每个颜色
    turtle.circle(10) #画圆圈
    turtle.right(angle) #画笔向右转
    turtle.forward(10) #向前10px

turtle.penup() #抬起画笔
turtle.goto(-150, 50) #来到位置-150,50
turtle.color("pink") #设置颜色
turtle.pendown() #放下画笔
turtle.write("Happy Birthday 王老师!", None, None, "24pt bold") #写文字
turtle.color("black") #设置颜色

turtle.color("pink") #设置颜色

turtle.write("Happy Birthday 王老师!", None, None, "24pt bold") #写文字
```
