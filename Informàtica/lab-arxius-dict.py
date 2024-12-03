import string
string.ascii_letters # mostra totes les lletres

import math

math.pi # numero pi

def suma(a, b):
    return a+b
def mult(a, b):
    return a*b

# pots importar fitxer (dins la mateixa carpeta) per utilitzar les seves funcions
#from doc import func --> importa la funció
#from doc import * --> importa totes les funcions

#repàs fitxers i diccionaris:

#arxiu = open("arxiu.txt", "r") --> # r--> read r+--> w --> write
#for linia in arxiu:
#    print(linia)
#print(arxiu.readlines()) --> escriu totes les linies seguides
#arxiu.close()

#print(arxiu.readline()) --> escriu la primera linia
#print(arxiu.readline()) --> escriu la segona linia
#print(arxiu.read()) --> escriu tot l'arxiu

#arxiu = open("arxiu_dos.txt", "w") --> crea arxiu_dos i obre el fitxer en mode escriptura
#arxiu_dos.write("Bon dia\n") --> escriu "Bon dia" en una linia
#arxiu_dos.close()

#arxiu = open("arxiu", "r+") --> mode llegeix i escriu
#arxiu = open("arxiu", "a") --> escriu al final del document

#contar paraules
#arxiu = open("arxiu.txt", "r")
#for linia in arxiu: --> escriu un caracter per linia
#    for caracter in linia:
#        print(caracter) 
#for linia in arxiu: --> escriu una linia per linia
#   print(f"La linia és: {linia})

diccionari = {}
for linia in arxiu:
    paraula = ""
    for caracter in linia: #per cada lletra
        if caracter == " ": # si hi ha un espai --> comença una nova paraula
            paraula_check = paraula.lower() #passa totes les lletres a minuscula pq conti totes les paraules sense diferenciar majuscula de minuscula.
            if diccionari.get(paraula_check,0): #si la paraula ja esta al diccionari
                diccionari[paraula_check] += 1 #suma 1 al contador de la paraula
            else: #si no està al diccionari
                diccionari[paraula_check] = 1 #afegeix el contador de la paraula a 1
            paraula = "" #reinicia la variable paraula
        else:
            paraula += caracter #afegeix la lletra a la paraula

for k,v in diccionari.items():
    print(f"La paraula {k} ha sortit {v} cops") #per cada item del diccionari escriu quantes vegades ha sortit cada paraula 


#EOL 8.1
"""
Volem muntar un sistema d'autentificació d'usuaris. Per tal de fer això cal desenvolupar un menú on ens permeti crear, esborrar i 
editar usuaris amb tota la seva informació referent.
A partir d'un diccionari d'usuaris hem de guardar per cada un el nom, l'adreça i la paraula clau que farà servir per accedir al sistema. 
En el menú tindrem les següents opcions :
    Afegir un usuari : Es demana el nom d'usuari, el nom complert, el correu electrònic, el telèfon, l'adreça i la paraula clau
    Esborrar un usuari : Es demana el nom d'usuari
    Modificar un usuari : Es demana el nom d'usuari i es permet canviar les dades

Un cop tenim la funcionalitat bàsica afegirem guardar a disc tota la informació de manera que poguem tenir unes dades. Per això afegirem al menú :

    Guardar a disc : Es demana el nom del fitxer que s'usarà i es guarda en ell la informació del diccionari.
    Llegir de disc : Es demana el nom del fitxer que es llegira i crearà el diccionari

Finalment crearem un altra programa en python que ens demani una nom d'usuari i una paraula clau i ens indiqui si està validat. Per tal de 
saber quin fitxer de dades s'usa es passarà per parametre.

[OPCIONAL] De forma opcional caldria buscar una manera de guardar la paraula clau d'una forma encriptada en el fitxer de dades.
"""

def autentificacio():
    #menu
    opcio = input("1. Afegeix un usuari /n2. Esborrar un usuari/n 3. Modificar un usuari")
    if opcio == 1:
        #Es demana el nom d'usuari, el nom complert, el correu electrònic, el telèfon, l'adreça i la paraula clau
    elif opcio == 2:
        #Es demana el nom d'usuari
    elif opcio == 3:
        #Es demana el nom d'usuari i es permet canviar les dades
    else: 
        print("La funcionalitat escollida no està disponible")


#EOT 8.4
def diccioLlista(llista):
    """
    >>> diccioLlista([["Jan", "Li fa pal"], ["Aina", "No es pot menjar"]])
    {"Jan": ["Li fa pla"], "Aina": ["No es pot menjar"]}
    >>> diccioLlista([["numeros", 3, 4, 5],["lletres"], "a", "b", "c"]])
    {"numeros": [3,4,5], "lletres": ["a", "b", "c"]}
    """
    diccionari
