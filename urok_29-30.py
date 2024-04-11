d = {
    "key":"value",
    "Машина":"Лада гранта",
    "Катя":"Данилова"
}
# d2 = dict()
# print(d)
#
# print(type(dict))
# print(type(d2))
# print(d["key"])
# print(d["Машина"])
d["key"] = "memory"
print(d["key"])
#
print(d.pop("Катя"))
print(d, '\n')
print(d.popitem(), '\n')
print(d)
#
# d["man"] = "Igor"
# print(d)
# d["woman"] = "Vera"
# print(d)
# d.update({"car":"volga"})
# print(d)
#
key = "first"
val = "value"
d.update({key:val})
print(d)
#
# for i in d:
#     print(i)
#
for i in d.values():
    print(i)
for i in d.keys():
    print(i)
#
# for k, v in d.items():
#     print(k, "-", v)
#
print(d.get("second")) ## показывает, есть ли вообще такое значение
print(d.get("first"))

