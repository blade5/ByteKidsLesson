# 改变背景颜色
```python
import turtle

turtle.Screen().bgcolor("blue")

t = turtle.Turtle() # 得到小乌龟
t.forward(100)
```

# 修改画笔颜色
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.pencolor("green")
t.forward(100)
```

# 修改画笔粗细
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.pensize(5)
t.forward(100)
```

# 填充颜色
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.begin_fill()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.end_fill()
```

# 改变填充颜色
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.fillcolor("orange")
t.begin_fill()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.end_fill()
```

# 画圆
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.fillcolor("red")
t.pensize(3)
t.pencolor("blue")
t.begin_fill()

for i in range(360):
    t.forward(1)
    t.right(1)

t.end_fill()
```
