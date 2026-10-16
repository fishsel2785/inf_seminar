sklad = [20, 35, 12, 0, 50, 0, 8]

print()
print(f"Sklad (kusy): {sklad}")

print()
print(f"Počet vypredaných druhov tovaru: {sklad.count(0)}")

sklad.remove(0)
sklad.remove(0)
print()
print(f"Po odstránení vypredaných druhov: {sklad}")

sklad.insert(0,100)
sklad.append(15)
print()
print(f"Po pridaní nových druhov: {sklad}")

print()
print(f"Najviac kusov: {max(sklad)}")
print(f"Najmenej kusov: {min(sklad)}")
print(f"Spolu kusov: {sum(sklad)}")

zoradenie = sklad.sort(reverse=True)
print()
print(f"Zoradené od najväčšieho: {zoradenie}")

print()
print(f"Druhý najpočetnejší druh: ")