pocet = int(input("pocet dni: "))

spolu=0

for i in range(1,pocet+1):
    den=int(input(f"trzba za den {i}: "))
    spolu +=den

priemer=spolu/pocet

print(f"celkova trzba: {spolu}")
print(f"priemerna denna trzba: {priemer}")
