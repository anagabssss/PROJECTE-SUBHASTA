#esquema de recorregut (dades seqüencials, s'han de tractar tots els elements)
a = "xavier"
a[0] = "x"
a[1] = "a"
a[-3] = "i"
index = 0
a[index] = "x"
index +=1
a[index] = "a"
index +=1
a[index] = "v"

index = 0
cadena = "qualsevol"
vocals = 0
while index < len(cadena):
    if cadena[index] in "aeiou":
        vocals += 1
    index += 1 
print(vocals)

for caracter in cadena:
    if caracter in "aeiou":
        vocals += 1
    print(vocals)

#esquema de cerca (dades seqüencials, no ha de tractar tots els elements, només si conté un element.)
"""
Demana 10 nombres a un usuari i si introdueix -1 stop
"""
menys_un_trobat = False
numeros_introduits = 0
while not menys_un_trobat and numeros_introduits < 10:
    x = int(input("Introdueix un número: "))
    if x == -1:
        menys_un_trobat = True
    numeros_introduits += 1

for numero in range(10):
    x = int(input("Introdueix un número: "))
    if x == -1:
        break

a = "hola"
a_trobada = False

for caracter in a:
    if caracter == "a":
        a_trobada = True
        break
    else:
        a_trobada = False

if a_trobada:
    print("Hi ha la lletra 'a' en la cadena.")
else:
    print("No hi ha la lletra 'a' en la cadena.")
