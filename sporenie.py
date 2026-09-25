odlozene = float(input("kolko si chces odlozit kazdy mesiac?: "))

mesiac = int(input("kolko mesiacov budes sporit?: "))

nasporene = 0

for i in range(1,mesiac+1):
    nasporene += odlozene
    print(f"Po {i} mesiaci: {nasporene}")

print(f"nasporene spolu: {nasporene}")