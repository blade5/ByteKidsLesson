# 打印 一一得一
for i in range(1, 10):
    print(f"1 x {i} = {1 * i}", end="\t")
print()



#-*-coding: utf-8-*-
import time

def print_picture(words):
    for y in range(12, -12, -1):
        line = []
        letters = ''
        for x in range(-30, 30):
            expression = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            if expression <= 0:
                letters += words[(x - y) % len(words)]
            else:
                letters += ' '
        line.append(letters)
        print("".join(line))
        time.sleep(0.1)


words = input("输入一句你想说的话: ")

print_picture(words)

