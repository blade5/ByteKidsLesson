import turtle

turtle.shape('turtle')
screen = turtle.Screen()  # 获取画布
screen.bgcolor('yellow')  # 设置画布背景颜色

# fun里面的函数体是可以自己定义的
def fun(x, y):
    print(x, y)
    turtle.goto(x, y)

screen.onclick(fun)
screen.mainloop()  # 使画布运行完之后不要关闭