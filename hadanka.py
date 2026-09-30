import random

cisloh = random.randint(1,10)



pokusy = 3


while pokusy>0:
    cislo = int(input("hadaj cislo od 1 do 10: "))
    if cislo == cisloh:
        print("uhadla si")
        break

    else:
        print("neuhadla si, mas este jeden pokus")
    pokusy-=1

if pokusy==0:
    print(f"neuhadla si, bolo to cislo {cisloh}")

