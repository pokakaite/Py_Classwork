import random

where = ["Из-за дерева","Из кустов","Сверху","Сзади","Из кареты"]
what = ["напал","упал","выпрыгнул","выскачил","свалился","вылетел","выкинули"]
who = ["гоблин","марадер","вор","зомби","вурдалак","леший","вампир","бес","рысь"]

print("Доброго дня путник ты начал свое приключение! Удачи в этом нелегком пути!")

player = {
    "Здоровье" : 100,
    "Атака" : 2,
    "Мана" : 0,
    "Оружие" : "Палочка",
    "Уровень" : 1,
    "Инвентарь" : {"Палочка" : 1}
}

enemy = {
    "Здоровье" : 0,
    "Атака" : 0,
    "Мана" : 0,
    "Оружие" : 0,
    "Уровень" : 0,
    "Инвентарь" : {}
}

tools = {
    "лук" : 5,
    "меч" : 10,
    "топор" : 15,
    "кирка" : 8,
    "мотыга" : 4,
    "вилы" : 7,
    "кулаки" : 2,
    "молот" : 6,
    "бита" : 6,
    "нож" : 3,
    "палка" : 1,
    "граната" : 30,
    "сюрикен" : 3
}

def menu():
    choice = int(input("Что вы будете делать? - \n"
                       "1 - Ататковать \n"
                       "2 - Бежать \n"
                       "3 - Инвентарь \n"
                       "4 - Выйти\n"))
    return choice

def stats(death = "Ваше текущее состояние"):
    print(f''' {death} -
    "Здоровье": {player["Здоровье"]},
    "Атака": {player["Атака"]},
    "Мана": {player["Мана"]},
    "Оружие": {player["Оружие"]},
    "Уровень": {player["Уровень"]}''')
    print("В инвентаре хранится: ", end="")
    for i in player["Инвентарь"]:
        print(i, end=", ")
    print('\n')
def enemy_gen(lvl):
    k = []
    for i in tools.keys():
        k.append(i)
    tool_ch = random.choice(k)
    enemy = {
        "Здоровье": random.randint(1, 50 * lvl * 0.1),
        "Атака": random.randint(1, 10 + (10 * lvl * 0.1)),
        "Мана": random.randint(1, 10 + (10 * lvl * 0.1)),
        "Оружие": tools[tool_ch],
        "Уровень": lvl-1,
        "Инвентарь": {
            tool_ch : tools[tool_ch]
        }
    }
    return enemy

def event():
    print("\n\n", random.choice(where), random.choice(what), random.choice(who))

def fight(player, enemy):
    player["Здоровье"] = player["Здоровье"] - (enemy["Атака"] + enemy["Оружие"])
    enemy["Здоровье"] = enemy["Здоровье"] - (player["Атака"] + player["Инвентарь"][player["Оружие"]])

    stats()
    ch = int(input('''Что вы хотите сделать?
                   1 - Атаковать
                   2 - Бежать
                   '''))
    if ch == 2:
        return run(player)
    if player["Здоровье"] <= 0:
        print("Вы проиграли :(.")
        stats(death="Ваше состояние после смерти -")
        return
    elif enemy["Здоровье"] <= 0:
        print("Ваш уровень повышен. Вы победили врага!")
        player["Здоровье"] += player["Здоровье"] * player["Уровень"] * 0.1
        player["Уровень"] += 1
        player["Мана"] += player["Уровень"] * 0.1
        player["Атака"] += player["Уровень"] * 0.1
        player["Инвентарь"].update(enemy["Инвентарь"])
        stats()
        return player
    else:
        return fight(player, enemy)

def run(player):
    player["Здоровье"] += 5
    return player

def tool(player):
    k = []
    for i in player["Инвентарь"].keys():
        k.append(i)
    for i in range(len(k)):
        print(f"{i+1} - {k[i]} с атакой {player['Инвентарь'][k[i]]}")

    t = int(input("Какое оружие выберите - "))
    player["Оружие"] = k[t-1]
    return player

def play(player):
    event()
    stats()
    ch = menu()
    if ch == 1:
        enemy = enemy_gen(player["Уровень"])
        fight(player, enemy)
    elif ch == 2:
        run(player)
    elif ch == 3:
        tool(player)
    elif ch == 4:
        stats()
        return
    return play(player)
play(player)
