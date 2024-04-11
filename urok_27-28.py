l1 = ["Мама", "папа", "сестра", 'тетя', "брат"]
l2 = ["Мама", "брат", "тетя", "внук"]
l3 = ["брат", "тетя"]
l5 = ["Мама", "дядя"]

l4 = l1 + l2 + l3
# print(l4)
#
# s = set(l4)
# print(s)
# print(list(s))

st = "wedjejd"
s1 = set(l1)
s2 = set(l2)
s3 = set(l3)
s4 = set(l4)
s5 = set(l5)
# s6 = set("vfv")
# s7 = set({"vfv"})
# s8 = set((st,))
# print(s8)
# print(s6)
# print(s7)
# print(s2)
# s2.intersection(s1)
# print(s2)
# s2.intersection_update(s1, s3)

print(f"{s1} - s1")
print(f"{s2} - s2")
# print(f"{s3} - s3")
# print(f"{s4} - s4")

print(s2.symmetric_difference(s1))
print(s2)

print(s1.union(s2))
# print(s2.isdisjoint(s1))
# print(s1)
# print(s2.issubset(s1)) ## проверяет, есть ли элементы s2 в s1 True
# print(s1.issubset(s2)) ## проверяет, есть ли элементы s1 в s2 False
#
# print(s5.isdisjoint(s3)) ## проверяет, полностью ли два множества различны True
#
# print(s2.issuperset(s1)) ## falss
# print(s1.issuperset(s2)) ## true
#
# print(s1)
# print(s1.pop())
# print(s1)
# print(s1.remove("Мама"))
# print(s1)


# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.update(s2))
# print(s1.difference_update(s3, s2))
# print(s1)
# s1 = list(s1)
# print(s1[0])
#
# s = set(l4)
# for i in s:
#     print(f"{i} - встречается - {l4.count(i)} раза")