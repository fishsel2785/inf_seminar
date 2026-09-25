treningy = int(input("pocet treningovych dni: "))

spolu=0

for i in range(1,treningy+1):
    km = float(input(f"km v den {i}: "))
    spolu+=km
    print(f"doteraz: {spolu}")

print(f"vzdialenost: {spolu}")