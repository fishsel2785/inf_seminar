import random

zoznam = []

pocet = int(input("zadaj pocet prvkov zoznamu: "))

for i in range(pocet):
    zoznam.append(random.randint(1,100))

print(zoznam)
