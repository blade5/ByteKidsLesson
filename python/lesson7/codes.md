# 第一个例子

```python
name = input("你叫什么名字啊? ")
print(f"你好, {name}, 很高兴认识你!")
```

# 追加一个问题

```python
word = input("> ")

if word == "How old are you?":
    print("I am 18!")

if word == "What's your name?":
    print("My name is Siri.")
```

# 使用循环

```python
while True:
    word = input("> ")

    if word == "How old are you?":
        print("I am 18!")
    if word == "What's your name?":
        print("My name is Siri.")
```

# 加入退出语句

```python
while True:
    word = input("> ")
    if word == "Byebye":
        print("See you next time")
        break
    if word == "How old are you?":
        print("I am 18!")
    if word == "What's your name?":
        print("My name is Siri.")
```

# 完整版本

```python
ANSWERS = {
  "hello": "Hello, 我是Siri, 我能为你做什么呢? ",
  "how old are you?": "I am 24."
}

while True:
    word = input("> ")

    if word == "byebye":
        break
    elif word in ANSWERS:
        print(ANSWERS[word])
    else:
        print("我听不懂你在说什么, 请重新一遍")
```
