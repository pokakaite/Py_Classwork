# name = "\\dir\\file"
# name1 = r"\dir\file"
# name2 = r"text.txt"
# f = open(name2, "w")
# f.close()
# f = open(name2, "r")
# print(f.read())
# f = open(name2, "a")
# f.close()
# f = open(name2, "at")
# print(f.write("asdfg"))
# f.close()
# f = open(name2, "w+")
# f = open(name2, "r+")

# try:
#     poem = r"text.txt"
#     f = open(poem, "r", encoding='UTF-8')
#     print(f.write('''
# Среди других играющих детей
# Она напоминает лягушонка.
# Заправлена в трусы худая рубашонка,
# Колечки рыжеватые кудрей
# Рассыпаны, рот длинен, зубки кривы,
# Черты лица остры и некрасивы.
# Двум мальчуганам, сверстникам её,
# Отцы купили по велосипеду.
# Сегодня мальчики, не торопясь к обеду,
# Гоняют по двору, забывши про неё,
# Она ж за ними бегает по следу.
# Чужая радость так же, как своя,
# Томит её и вон из сердца рвётся,
# И девочка ликует и смеётся,
# Охваченная счастьем бытия.
# Ни тени зависти, ни умысла худого
# Ещё не знает это существо.
# Ей всё на свете так безмерно ново,
# Так живо всё, что для иных мертво!
# И не хочу я думать, наблюдая,
# Что будет день, когда она, рыдая,
# Увидит с ужасом, что посреди подруг
# Она всего лишь бедная дурнушка!
# Мне верить хочется, что сердце не игрушка,
# Сломать его едва ли можно вдруг!
# Мне верить хочется, что чистый этот пламень,
# Который в глубине её горит,
# Всю боль свою один переболит
# И перетопит самый тяжкий камень!
# И пусть черты её нехороши
# И нечем ей прельстить воображенье, —
# Младенческая грация души
# Уже сквозит в любом её движенье.
# А если это так, то что есть красота
# И почему её обожествляют люди?
# Сосуд она, в котором пустота,
# Или огонь, мерцающий в сосуде?'''))
#     f.close()
# except Exception as exc:
#     print(exc, "Ошибка работы")
#     print(exc.errno, "Ошибка работы")

# try:
#     poem = r"text.txt"
#     f = open(poem, "r+", encoding='UTF-8')
#
#     print(f.read())
#     print(f.readline())
#
#     print(f.readlines(30))
#
#     for i in range(60):
#         print(f.readline())
#
#     or
#
#     st = f.readline()
#     while st != "":
#         print(st)
#         st = f.readline()
#     f.close()
#
#     st = f.readlines(30)
#     for i in st:
#         print(i)
# except Exception as exc:
#     print(exc, "Ошибка работы")
#     print(exc.errno, "Ошибка работы")

# try:
#     name = r"text.txt"
#     src = open(name, "r+", encoding='utf-8')
#     dst = open("text2.txt", "w+", encoding='utf-8')
#     dst.write(src.read())
#     dst.close()
#     src.close()
# except Exception as exc:
#     print(exc, "Ошибка работы")
#     print(exc.errno, "Ошибка работы")

with open('text.txt', 'r+', encoding='utf-8') as t:
    print(t.read())
    t.write("srg")
    print(t.read())