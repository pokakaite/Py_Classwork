var = 1
var1 = 10

a = 1
b = 10


def first():
    pass


print(first())


def first(var, var1):
    res = var + var1
    return res


print(first(1, 10))


def first(*args):
    res = args[0] + args[1]
    return res


print(first(1, 10))


def first(*args):
    res = 0
    for i in args:
        res += i
    return res


print(first(1, 2, 3))


def second(var=10, var1=20):
    res = var + var1
    return res


print(second())


def second(*vars, var=10, var1=20):
    res = 0
    for i in vars:
        res += i
    return res


print(second(10, 201, var1=b, var=10))

slovar = {"key": "value", "phone": "89061025666", "name": "Kate"}


def third(*args, vars, **kwargs):
    res = 0
    for i in args:
        res += i
    print(res)

    for i in kwargs:
        print(i, end=" - ")
        print(kwargs[i], end=', ')
    print()

    for i in vars:
        print(i, end=" - ")
    return 1


third(10, 20, 10, vars=[10, 20], name="Da", address="Ufa", mu="asdf")

import random
choice = random.randint(1, 100)
print(choice)

print('\n')

# Задание 1
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't let the noise of others' opinions
# drown out your own inner voice.”
# Steve Jobs

def func(*args):
    print(args[0] + '\n' + args[1] + '\n' + args[2].center(75))
func("Don't let the noise of others' opinions", "drown out your own inner voice.", "Steve Jobs")

print('\n')
# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все нечетные числа
# между ними.

def func1(*args):
    print("Все нечётные числа - ", end='')
    for i in range(args[0], args[1]):
        if i % 2 != 0:
            print(i, end=', ')
func1(10, 20)

print('\n')

# Задание 3
# Напишите функцию, которая отображает горизонатальную или вертикальную линию из некоторого символа.
# Функция принимает в качестве параметра: длину линии,
# направление, символ.

def func3(*args):
    for i in range(args[0]):
        if args[1] == 'вертикально':
            print(args[2].center(100))

    if args[1] == 'горизонтально':
        print(args[2] * args[0])
func3(5, 'вертикально', '$')

print('\n')

# Задание 4
# Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве
# параметров.

def func4(*args):
    nums = []
    minNum = args[0]
    maxNum = args[0]
    for number in args:
        if number < minNum:
            minNum = number
    for number in args:
        if number > maxNum:
            maxNum = number
    print(maxNum)
func4(1, 2, 3, 4)

print('\n')

# Задание 5
# Напишите функцию, которая возвращает сумму чисел
# в указанном диапазоне. Границы диапазона передаются
# в качестве параметров.

def func5(*args):
    res = 0
    for i in range(args[0], args[1]):
        res += i
    print(res)
func5(10, 13)

print('\n')

# Задание 6
# Напишите функцию, которая проверяет является ли
# число простым. Число передаётся в качестве параметра.
# Если число простое нужно вернуть из метода true, иначе
# false.

def func6(x):
    res = 0
    for i in range(2, x // 2 + 1):
        if (x % i == 0):
            res = res + 1
    if (res <= 0):
        print('true')
    else:
        print('false')
func6(7)

# Задание 7
# Напишите функцию, которая проверяет является
# ли шестизначное число «счастливым». Число передаётся в качестве параметра.
# Если число счастливое нужно вернуть из функции true, иначе false.
# «Счастливое шестизначное число» — это число у которого сумма первых трёх цифр равна сумме трёх вторых
# цифр. Например, 123420 – счастливое 1+2+3 = 4+2+0, а 723422 - несчастливое 7+2+3 != 4+2+2

def func7(x):
    y = str(x)
    sr = len(str(y))//2
    sum1 = 0
    for i in range(0, sr):
        sum1 += int(y[i])
    sum2 = 0
    for i in range(sr, len(str(y))):
        sum2 += int(y[i])

    if sum1 == sum2:
        print("Число счастливое")
    else:
        print("Число несчастливое")
func7('123321')