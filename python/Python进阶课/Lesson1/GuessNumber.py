#-*-coding: utf-8-*-
import random
name = input("输入你的名字: ")
number_to_guess = random.random(0, 20)

while(True):
    guess = input("猜我想的数: ")

    if int(guess) > number_to_guess:
        print("猜大了")

    if int(guess) < number_to_guess:
        print("猜小了")

    if int(guess) == number_to_guess:
        print(f"你真聪明, {name}")
        break
