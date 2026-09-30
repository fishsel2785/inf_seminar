import random

cisloh = random.randint(1,10)

cislo = int(input("zadaj cislo od 1-10: "))

if cislo == cisloh:
    print("uhadla si")

else:
    print(f"neuhadla si, bolo to cislo {cisloh}")