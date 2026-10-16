import random

zoznam = []

pocet = int(input("zadaj pocet prvkov zoznamu: "))

for i in range(pocet):
    zoznam.append(round(random.uniform(1,100),2))
    


print(zoznam)


