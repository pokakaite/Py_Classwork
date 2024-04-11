# a = [61, 74, 58]
# b = [94, 85, 16]
# print(sorted(a))
# print(b.sort())
# print(a)
# print(b)
#
#
# word = ['Student', 'Ambulance', 'Banana']
# list.sort(word)
# print(word)
# list.sort(word, reverse=True)
# print(word)
#
#
# list.sort(word, key = lambda word: len(word))
# print(word)
# list.sort(word, key = lambda word: len(word), reverse=True)
# print(word)
#
#
# a = 2
# b = 3
# c = 6
# a, b = b, a
# a, b, c = c, a, b
# print(a)
# print(b)
# print(c)


import random

l = []

def sp(x):
    for i in range(20):
        yield random.randint(0, 20)
print(sp(l))

def sor(x):
    li = list(x)
    li.sort()
    print(li)
sor(sp(l))



