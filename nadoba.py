import random

nadrz = int(input("kolko l vody sa zmesti do nadrze?: "))

voda = 0

den = 0

kapacita = 0

while voda<nadrz:
    dazd = random.randint(5,25)
    voda+=dazd
    den+=1
    kapacita+=1
    print(f"den {den}: pribudlo {dazd} litrov.")
    print(f"v nadrzi: {voda} litrov.")

print(f"naplnenie za {kapacita} dni.")