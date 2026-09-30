pocet = int(input("kolko zakaznikov chces zadat?: "))

for i in range(1,pocet+1):
    print(f"zákazník: {i}")
    vek = int(input("vek: "))
    if vek <= 15:
        print("vstup zamietnuty")
    else:
        print("vstup povoleny")

    