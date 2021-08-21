import turtle
turtle.shape('turtle')
screen=turtle.Screen() #获取画布
screen.bgcolor('yellow') #设置画布背景颜色
#onkey方法需要两个参数，onkey(fun,key)一个是函数fun，另外一个是键盘上的键位key
#函数fun不需要参数
def fun():
	screen.bgcolor('red')
screen.onkey(fun,'r')#当按下r键，就执行fun，严格区分大小写
#设置不同的函数就可以做到执行不同的效果
def fun1():
	turtle.forward(100)
def fun2():
	turtle.circle(100)
screen.onkey(fun1,'a')
screen.onkey(fun2,'b')
screen.listen() #鼠标单击画布，设置焦点，，开始收集键盘事件，如果没有本行代码，按下r键是没有反应的，单击画布开始执行
screen.mainloop()
