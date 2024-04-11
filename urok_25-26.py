l1 = (i for i in range(0, 5))
l2 = (i for i in range(5, 10))
print(l1, l2)

def show(l1, l2):
    l1 = list(l1)
    l2 = list(l2)
    for i in range(len(l1)):
        print(f"{l1[i]} - {l2[i]}")
    return 0

print(show(l1, l2))
