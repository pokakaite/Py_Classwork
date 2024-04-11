# v = int(input("Введите вашу скорость - "))
# if v>40:
#     if v-40>20:
#         print("Вы превысилы на более чем на 20 км/ч")
#         print("Вы оштрафованы")
#     print("Вы превысили скорость!")
# elif v<100:
#     print("Ваша скорость меньше 100")
# else:
#     print("Ваша скорость выше 100")

# print(bool(1) or bool(0))  #true
# print(bool(1) and bool(0))  #false
# print(bool(0) or bool(0))  #false
# print(bool(0) and bool(0))  #false
#
# print(651 != 0)
#
#
# # Спросить у пользователя его скорость. Затем определить планету, куда он хочет полететь.
# # Рассчитать время, за которое он туда доберется. Если время больше 10 лет, предложить улучшить его космолет.
#
# s = int(input("Введите скорость космолета - "))
# pl = input("На какую планету хотите полететь? - ")
# mer = "Меркурий"
# dist_mer = 176.47 * 1000000
# t_dist_mer = dist_mer / s
#
# ven = "Венера"
# dist_ven = 196.11 * 1000000
# t_dist_ven = dist_ven / s
#
# zem = "Земля"
# dist_zem = 0
#
#
# mar = "Марс"
# dist_mar = 353.2 * 1000000
# t_dist_mar = dist_mar / s
#
#
# jup = "Юпитер"
# dist_jup = 720.46 * 1000000
# t_dist_jup = dist_jup / s
#
#
# sat = "Сатурн"
# dist_sat = 1.5751 * 1000000000
# t_dist_sat = dist_sat / s
#
#
# uran = "Уран"
# dist_uran = 2.8859 * 1000000000
# t_dist_uran = dist_uran / s
#
#
# nep = "Нептун"
# dist_nep = 4.5585 * 1000000000
# t_dist_nep = dist_nep / s
#
#
#  # if s > 10 лет то
# if (pl == mer and t_dist_mer > 87840) or (pl == ven and t_dist_ven > 87840):
#     print("Улучшите самолет")
# else:
#     print("Летите")

# while (Условие):
#     Инструкция

# i=1
# while 1<100:

# for i in [1,2,3] :
#     print(i)
#
# for i in "Katya":
#     print(i)
#
# for i in "kate", "vane":
#     print(i) # показал два слова
#
# for i in "kate", "vane":
#     for m in i:
#         print(m) # перебрал буквы у обоих слов
#
# for i in range(10):
#     print(i) # перебирает от 0 до 9
#
# for i in range(5, 10):
#     print(i) # перебирает от 5 до 9
#
# for i in range(0, 1000, 3):
#     print(i) # перебирает числа через три
#
# print(10 if 10>20 else 20)


# m = 10023
# for _ in range(1, 20, 3):
#     m += 3
#     print(3)

# print([" a " for _ in range(10)]) # [' a ', ' a ', ' a ', ' a ', ' a ', ' a ', ' a ', ' a ', ' a ', ' a ']
# l = [" a " for _ in range(10)]
# for i in l:
#     print(i, end="")  #  a  a  a  a  a  a  a  a  a  a
#
# s = "Hello World!"
# print(s[0:10:1]) # Hello Worl
# print(s[12:0:-1]) # !dlroW olle

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")

# i = 1
# while i<100:
#     if i>50:
#         break
#     if i<50:
#         continue
#     i += 1
#     print(i)

i = 1
while i<50:
    print(i)
    i += 1
    if i>50:
        break
else:
    print("Я всё выполнил!")
