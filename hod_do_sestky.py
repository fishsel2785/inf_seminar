import random

cislo=0
hody=0

while cislo<6:
    cislo=random.randint(1,6)
    hody+=1
    print(f"hod: {cislo}")

print(f"sestka padla na {hody} hod.")