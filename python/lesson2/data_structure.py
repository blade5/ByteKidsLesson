#-*-coding: utf-8-*-

name = "大卫"
age = 18
gender = "男性"
myself = {
    "name": name,
    "age": age,
    "gender": gender,
    "hobbies": ["打篮球", "打乒乓球"]
}

print("我的名字是" + myself["name"])
print("我的年龄是" + str(myself["age"]))
print("我的爱好是" + myself["hobbies"][0] + "和" + myself["hobbies"][1])
