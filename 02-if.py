# 判断语句
MyWeight = 95
canRide = True
if MyWeight > 80:
    print("超过体重限制")
    canRide = False
print(canRide)

# 缩进：python要求同一层级缩进

# 循环
numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    print(number)
print("输出2-6项：")
for number in numbers[1:6]:
    print(number)

# 遍历，应用：累加与计数器
studentAge = {"Gary": 14, "Ada": 13, "Jack": 15, "Max": 14, "Tim": 14}
for key in studentAge:
    studentAge[key] = 16
print("输出studentAge：")
print(studentAge)

# while循环
nameList = ["Max", "Tom", "Jim", "Ken", "Kim", "Tim"]
counter = 0
while counter < 5:
    print(nameList[counter])
    counter += 1
#break,continue