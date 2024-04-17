import json
import pickle
a, b, c = 1, 2, 3

a = [1, 2, 3, 4, 5, 6]
a = (1, 2, 3, 4, 5, 6)
a = 1, 2, 3, 4, 5, 6

a, *b, c = a

print(a)
print(b)
print(c)

d = {
    'name': "katya",
    'lastname': 'danilova',
    'year': 2002,
    'day' : 5
}

a, b, *c = d

print(a)
print(b)
print(c)
print()

for key, value in enumerate(d): ######### нумерует
    print(key, '-', value)

for index, key in enumerate(d): ######### нумерует
    print(index, '-', key, '-', d[key])


*s, = d.keys(), d.values()
print(s)
print(s[0])
print(s[1])

a,_,c,_,*t = a
print(a)
print(c)
print(t)


d1 = {
    'name': "katya",
    'lastname': 'danilova',
    'year': 2002,
    'day' : 5
}

d2 = {
    'name1': "tanya",
    'lastname2': 'danilova',
    'year3': 1998,
    'day4' : 1
}

d3 = {**d1, **d2}
print(d3)


d4 = d1.update(d2)
print(d1)









# class Man:
#     def __init__(self):
#         self.name = 'Katya'
#         self.lastname = 'Danilova'
#         self.year = 2002
#
# ob = Man()
#
# print(ob.__dict__)
# boo = ob.__dict__
# with open("j.json", "w") as f:
#     json.dump(boo, f) ######### сохраняет инфу в файл
#
# with open("j.json", "r") as f:
#     n = json.load(f)
#
# print(n, type(n))
#
#
#
# with open("j.pkl", 'wb') as f:
#     f.write(pickle.dumps(ob)) ### сохраняет инфу в переменную
#
# with open("j.pkl", 'rb') as f:
#     m = pickle.load(f)
#
# print(m, type(m))







