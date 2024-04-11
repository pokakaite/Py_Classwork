import random
#
# l = random.randint(0, 10) ## ctrl + тыкнуть на рандинт
# print(l)
#
# def choice():
#     return random.choice([0, 10, 4, 854, 78])
# print(choice())
import random
# from random import choice, randint
#
# print(choice([1, 2, 3, 4]))
# print(randint(1, 20))







from random import *

# def choice(a):
#     return True
# print(choice([1, 23, 45]))
#
#
#
#
#
# import random as r
# print(r.randint(1,10))
#
#
#
#
#
# import random
# random.seed(0)
# print(random.random())
#
#
#
#
#
#
# from random import *
# # print(randrange(0, 100, 2))
# # print(randrange(100))
#
#
#
#
#
# print(choice('wdfwef'))
#
# print(sample([12,123,2,4,5,46,], 3))
# print(sample("efiefeifh", 3))
#
# import platform
#
# print(platform.platform(aliased = False, terse = False))
# print(platform.platform(aliased = True, terse = False))
# print(platform.platform(aliased = True, terse = True))
# print(platform.platform(0, 0))
# print(platform.uname())
# print(platform.processor())
# print(platform.release())




import tkinter

root = tkinter.Tk()

root.title("First window")
root.geometry("600x600+800+100")

def pres():
    t = en.get()
    l2 = tkinter.Label(text=t)
    l2.pack()

l1 = tkinter.Label(text="First window", background="red", font=("", 20))
l1.pack()

en = tkinter.Entry(width="60", border="5")
en.pack()

bt = tkinter.Button(text="press", command=pres)
bt.pack()
root.mainloop()









import turtle

t = turtle.Turtle()
turtle.shape("turtle")
t.speed(10)

t.forward(120)
t.right(140)
t.forward(120)
t.right(150)
t.forward(120)
t.right(140)
t.forward(120)
t.right(150)
t.forward(120)
t.up()

t.forward(100)

t.down()
t.left(40)
t.forward(100)
t.right(40)
t.forward(100)
t.right(90)
t.forward(100)
t.right(50)
t.forward(100)
t.right(50)
t.forward(100)
t.right(80)
t.forward(90)

t.up()

t.forward(100)

t.down()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.up()

t.forward(100)

t.down()


t.forward(100)
t.right(90)
t.forward(100)
t.right(135)
t.forward(140)
t.right(90)

t.up()

t.forward(350)

t.down()


turtle.done()