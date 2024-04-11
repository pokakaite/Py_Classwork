# st1 = "Hello World!"
# print(f"{st1:*^100}")
# # рез: ********************************************Hello World!********************************************

# import re
# userStr = "abcd abc efgh"
# match = re.search(r'\w{4}', userStr)
# print(match.group())

l = list()
l2 = []
l3 = ["first", 0, 3.2, "q"]
print(l)
print(l2)
print(l3)

for i in l3:
    print(i)

for i in l3:
    print(i, "-", type(i), "-", l3.index(i))

l3.remove(0)
print(l3)

print(l3.pop())
print(l3)

print(l3.pop(0)) # pop - удаляет элемент из списка
print(l3)

l.append("adfef")
print(l) # добавляет в конец

l3.insert(2, 'erfgr') # добавляет в то место, куда нужно
print(l3)

l[0] = "rfrfe"
print(l)

try:
    l[4] = "rg"
except IndexError:
    l.insert(4, "rg")

print(l)

l.clear()
l3 = []

l4 = l + l3
print(l4)

rooms = [1, 2, 3, 4]
students = [["Vasya", "Petya", "Igor", "Ira"], [], [], []]
count = 0
for i in rooms:
    print(i)
    for s in students[count]:
        print(s, end=", ")
    print()
    count += 1

l = [i for i in range(100)]
print(l)

l = [i*i for i in range(10)]
print(l) # тернарный опрератор

l = [range(10)]
print(l) ######### такое не сработает

l = [i*i for i in range(10) if i % 2 == 0]
l = l + rooms
print(l) # тернарный оператор
print(len(l))

print(l[3:1:-2])
print(max(l))
print(min(l))
print(sum(l)/len(l))

l3 = ["first", "q"]
print(sorted(l)) # отсортированный список
print(sorted(l, reverse=True)) # отсортированный список наоборот
print(sorted(l3, reverse=True))
print(l.index(16)) # находит только первое вхождение

l = ["Стерлитамак", "Уфа"]

print("Уфа" in l) # True

l1 = [1, 2, 3, 4, 5]
print(l1)
l2 = l1.copy()
print(l2 is l1)
l2[1] = "Hello"
print(l2)
print(l1)
l3 = list(l1)
print(l3)

print(set(l1 + l2))

price = [30, 60, 40, 50]
item = ["Шоколад", "Яйца", "Яблоки", "Конфеты"]
amount = [2, 3, 4, 5]
count = 0

x = -1
for i in item:
    x += 1
    print(i, ", ", "Цена -", price[x], ", количество -", amount[x])
    print("Итого - ", price[x] * amount[x])


