ciel = float(input("kolko si chces nasporit? "))

odklad = float(input("kolko si chces odkladat? "))

nasporene = 0

mesiac = 0

while nasporene < ciel:
    nasporene += odklad
    mesiac +=1
    print(f"mesiac {mesiac}: {nasporene}")

print(f"ciel dosiahnuty za {mesiac} mesiacov.")
