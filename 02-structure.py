# 1.tuple(元组)，顺序表 2.list 3.dict
# tuple(索引从0开始)
calender = ("1月1日", "1月2日", "1月2日", "1月2日")
print(calender[1])
print(calender[1] + calender[3])
# in运算
result = "1月1日" in calender
print(f"result：{result}")
print("1月1日" in calender)

print(calender)

# list
players = ["Kevin", "Tony", "Asum"]
print(players)

# 增删改查
print(players[1])
players.append(1)
players.insert(0, "Jony")
print(players.pop())
print(players.pop(2))

# 列表切片
print(players[0:2])

# dict
cart = {"超级苦咖啡": 1, "超级辣辣条": 3, "超想吃披萨": "售罄"}
print(cart["超级苦咖啡"])
# 元素删除
# 注意python里面没有null，而是None
cart.pop("超想吃披萨")
print(cart)
