# try:
#     a = int(input("Num 1 - "))
#     b = int(input("Num 2 - "))
#     res = a / b
#     str = 'Hello, world!'
#     if a > "10":
#         raise ValueError
#     print(res)
#     print(str[8])
# except ValueError:
#     print("Нужно ввести цифры")
# except IndexError:
#     print("Неверный индекс")
# except TypeError:
#     print("Неверный тип")
# except Exception:
#     print("Неверные данные")
# else:
#     print("All good")
# finally:
#     print("End")






# try:
#     num_User = int(input("Введите число от 1 до 100 - "))
#
#     if num_User > 100 or num_User < 1:
#         raise ValueError
#     if num_User % 3 == 0 and num_User % 5 != 0:
#         print("Fizz")
#     if num_User % 5 == 0 and num_User % 3 != 0:
#         print("Buzz")
#     if num_User % 3 == 0 and num_User % 5 == 0:
#         print("Fizz Buzz")
#     if num_User % 3 != 0 and num_User % 5 != 0 and num_User < 100 and num_User > 1:
#         print(num_User)
#
# except ValueError:
#     print("Число не в диапазоне")
# except TypeError:
#     print("Неверный тип")
# except Exception:
#     print("Неверный тип")
# else:
#     print("All good")
# finally:
#     print("End")






# try:
#     a = int(input("Num 1 - "))
#     if a < 1 or a > 100:
#         raise ValueError
#     try:
#         if a % 3 == 0 and a % 5 == 0:
#             print("Fizz Buzz")
#         elif a % 3 == 0:
#             print("Fizz")
#         else:
#             raise ValueError
#     except ValueError as vl:
#         try:
#             if a % 5 == 0:
#                 print("Buzz", "\n", vl)
#             else:
#                 raise ValueError
#         except ValueError as vl:
#             print(a, "\n", vl)
# except ValueError as vl:
#     print("Нужно указать число от 1 до 100", "\n", vl)
# except Exception:
#     print("Неверный тип")



try:
    while 1:
        a = input("Введите число - ")
        try:
            a = int(a)
        except ValueError:
            print("Вы ввели неверные данные!")
        else:
            raise ValueError
except ValueError:
    for i in range(8):
        print(f"{a} в степени {i} - {a**i}")
finally:
    print("Возведение в степень выполнено!")