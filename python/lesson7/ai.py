#-*-coding: utf-8-*-

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
