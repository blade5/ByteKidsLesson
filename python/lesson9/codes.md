# 初始化
```python
import turtle
t = turtle.Turtle() # 得到小乌龟
```

# 画直线
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.forward(100)
```

# 转向

```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.forward(100)

t.left(90)

t.right(90)
```

# 画方块
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
```

# 左转画方块
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
```

# 画三角形
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
```

# 画直角等腰三角形
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

t.forward(141)
t.left(135)
t.forward(100)
t.left(90)
t.forward(100)
```

# 画圆
```python
import turtle
t = turtle.Turtle() # 得到小乌龟

for i in range(360):
    t.forward(1)
    t.right(1)
```
