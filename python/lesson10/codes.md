# 画五角星

```python
import turtle
s = turtle.getscreen()
t = turtle.Turtle()

t.pencolor("red")
t.pensize(3)
t.fillcolor("yellow")
t.begin_fill()

for i in range(5):
    t.forward(100)

    t.right(180 - 36)

t.end_fill()
```

# 画彩虹

```python
import turtle
t = turtle.Turtle() # 得到小乌龟
t.pensize(22)
t.speed(10)
t.penup()
t.forward(150)
t.left(90)
t.pendown()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
r = 150
for color in colors:
  t.pencolor(color)
  t.circle(r, 180)
  t.penup()
  t.circle(r, 180)
  r = r - 15
  t.left(90)
  t.forward(15)
  t.right(90)
  t.pendown()
```
