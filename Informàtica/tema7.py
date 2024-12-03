#mòduls i fitxers
#fitxers

myFile = open("nom") #--> obre el fitxer nom i lin posa el nom file. el fitxer ha d'estar dins del mateix directori que el codi executat
#permisos per obrir r: read, w: write, r+: lectura i escriptura, a: append. afegeix al final del fitxer
#si intentes obrir un fitxer no existent amb permis W, crea el fitxer

myFile.write("hola\n") #escriu a sobre el fitxer
print(myFile.write("sadas\n")) #escriu el nombre de lletres
myFile.read() #llegeix el document
myFile.readline() #llegeix una linia
myFile.readlines() #llegeix totes les linies
myFile.close() #--> sempre s'ha de tancar el fitxer

#moduls

import sys
print(sys.argv) #--> type list. el primer element de la llista es el nom de l'arxiu. crea una llista d'un str separant els arguments en els espais

llista = sys.argv[1:] #--> treu el primer element de la llista pq es el nom de l'argument i no fa falta
suma = 0
for i in llista:
    suma += float(i)
print(suma)
#execució --> python3 argv 2 5 2 4 6 4 2 6 --> suma tots ele elements de la llista

