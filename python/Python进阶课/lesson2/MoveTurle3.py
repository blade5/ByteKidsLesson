import turtle
turtle.shape('turtle')
screen=turtle.Screen() #获取画布
screen.bgcolor('yellow') #设置画布背景颜色
#自定义前后左右键位分别对应执行的函数
def up():
	turtle.forward(50)
def back():
	turtle.backward(50)
def left():
	turtle.left(90)
def right():
	turtle.right(90)
#调用onkey函数
screen.onkey(up,'Up')
screen.onkey(back,'Down')
screen.onkey(left,'Left')
screen.onkey(right,'Right')
#单击鼠标焦点开始获取键盘事件
screen.listen()
#运行完毕后不关闭screen窗口
screen.mainloop()
