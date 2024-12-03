#cadenes de caracters
cadena = "hola"
#indexar una lletra del string str[index] (comencant per 0)
cadena[0] #retorna "h"
cadena[1] #retorna "o"
cadena[6] #retorna string index out of range
cadena[-1] #retorna 
#sobreescriure la variable a = a
#es poden concatenar (+)
#es pot convertir a enter o decimal --> int(var)    float(var)
len(cadena) #longitud de la cadena
cadena[len(cadena)-1] # --> retorna l'ultima lletra de la variable
#

cadena = "paquito"
print(cadena) #"paquito"
print (cadena[0]) #"p"
b = len(cadena) -1 #-1 pq es comenca per 0
a = 0
while a<= b:
    #a = 1 ..... len(cadena) -1
    print(cadena[a], end="") #end="" evita ENTER (ho escriu tot en una sola linia)
    a = a+1
print()
while b >= 0: #escriu "paquito del reves"
    print(cadena[b], end="") 
    print(cadena[b])
    b = b-1
print()

#for --> Bucle for, itera sobre una cadena de caracters indexan, valor per valor i trencant el bucle quan ja no n'hi ha cap més
cadena = "paquito"
for letra in cadena: #per cada caracter en la variable cadena ()
    print(letra, end="")
print()

#bucles for son finits

#slice var[inici:longitud slice] --> te un final
cadena[0] #"p"
cadena[0:3] #"paq"
cadena[0:] #"paquito"
cadena[:7] #"paquito"
cadena[0:50] #"paquito"

#in --> mira si "" esta dins de la variable. comprova si un str es substr d'un altre
"paq" in cadena #True

#comparacio cadenes >   <   =   ==

cadena.capitalize() # 
for i in cadena:
    print(i.capitalize()) #primera majuscula
print()
cadena = cadena.upper() #totes majuscules
print(cadena.lower()) #totes minusculas

print(cadena.find("o")) #escriu el lloc on esta "o"
print(cadena.fins("z")) # escriu -1 (no troba la variable)

for i in cadena: #escriu paquito sense les a
    if i =="a":
        continue
    print(i.capitalize())


for i in cadena: #escriu paquito sense les a
    if i =="a":
        continue
    print(i.capitalize())
    for i in cadena:
        print(i, end="")

cadena = "paquito"
print(cadena[0])
cadena_canviada = "l" + cadena[1:]
print(cadena_canviada) #"laquito"

z = ""
for caracter in cadena:
    if caracter == "q": #substitueix la "q" per "c"
        z = z+"c" #afageix "c" a la cadena
    elif caracter == "u": #substitueix la "u" per "h"
        z = z+"h" #afageix "h" a la cadena
    else:
        z = z+caracter # afageix el caracter a la cadena
print(z) # "pachito"

cadena = "grup30"
cadena_dos = "GRup30"
cadena[:3].upper() # "GRU"
cadena == cadena_dos #False --> Distingeix entre majuscules i minuscules
cadena.upper() == cadena_dos.upper() #True

cadena_canviada = cadena.replace("qu", "ch")
print(cadena_canviada) #"pachito"

str.strip() #elimina els espais en blanc de la cadena
cadena_canviada = cadena.strip()

str.startswith("str") #
comprova_cadena = cadena.startswitch("pa") #comprova si la cadena comenca per el str donat
print(cadena)
print(comprova_cadena)

cadena = "Món"
cadena_modificada = f"Hola {cadena}"
print(cadena_modificada) # --> "Hola Món"
