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
