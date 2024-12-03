import sys

diccionari = {}
print(sys.argv[1])

for lletra in sys.argv[1]:
    if lletra == "":
        continue
    elif diccionari.get(lletra):
        diccionari[lletra] +=1
    else:
        diccionari[lletra] = 1

tmp = list(diccionari.items())
tmp.sort()
for clau, valor in diccionari.items():
    print(f"{clau} {valor}")