# for i in range(5):
#     print(i)
#
# l = [ i*i for i in range(5) ]
# print(l)
#
# l = [ i for i in range(5) ]
#
# l1 = ( i for i in range(5) )
# print(l)
# print(l1)
#
# for i in l1:
#     print(i)
#
#
#
# def fun(n):
#     for i in range(n):
#         yield i
# print(fun(5))
#
# for i in fun(5):
#     print(i)
#
# def fun(n):
#     for i in range(n):
#         if i % 2 == 0:
#             name = "Иван" + str(i)
#             yield name
# print(fun(5))
#
# for i in fun(5):
#     print(i)


# import random
#
# user = input("Сколько хотите видеть имен? - ")
#
# l1 = ['Катя', 'Ирина', 'Маша', 'Алена', 'Даша', 'Таня']
# l2 = ['Данилова', 'Сидорова', 'Петрова', 'Воробьева', 'Кузнецова', 'Горбачева']
#
# def names(x, y, z):
#     for i in range(int(z)):
#         name = random.choice(x)
#         surname = random.choice(y)
#         yield name + ' ' + surname
#
# print(names(l1, l2, user))
#
# for i in names(l1, l2, user):
#     print(i)



#
# q = lambda: 2
# a = lambda x: x**2
# z = lambda x, y: x**y
# print(q())
# print(a(2))
# print(z(2, 3))


# def printfunc(args, fun):
#     for x in args:
#         print('f(', x, ')=', fun(x), sep='')
#
# printfunc([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
#
# l1 = [i for i in range(5)]
# l2 = list(map(lambda x: 2**x, l1))
# print(l2)
#
# for i in map(lambda x: x*x, l2):
#     print(i, end=" ")
#
# print()






# l1 = [i for i in range(10)]
#
# print(list(filter(lambda x: x % 2 == 0, l1)))
#
# l1 = [i for i in range(10)]
#
# print(list(map(lambda x: x % 2 == 0, l1)))
#
#
#
#
#
# def outer(par):
#     loc = par
#     def inner():
#         return loc + 5
#     return inner
# var = 1
# fun = outer(var)
# print(fun())






sp = ['*', '|']

count = -1
tab = 40

for i in range(0, 4):
    for s in list(filter(lambda x: x == '*', sp)):
        tab -= 1
        count += 2
        print(' ' * tab, s * count, end='\n')

count = 29
tab = 25

for i in range(0, 3):
    for s in list(filter(lambda x: x == '*', sp)):
        tab += 3
        count -= 6
        print(' ' * tab, s * count, end='\n')

count = 17
tab = 34

for i in range(0, 1):
    for s in list(filter(lambda x: x == '*', sp)):
        tab -= 1
        count -= 4
        print(' ' * tab, s * count, end='\n')

count = 17
tab = 34
tab2 = -5

for i in range(0, 3):
    for s in list(filter(lambda x: x == '*', sp)):
        tab -= 1
        count -= 4
        tab2 += 6
        print(' ' * tab, end='')
        print(s * (count // 2), ' ' * tab2, s * (count // 2), end='\n')