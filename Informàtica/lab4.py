#lab4

import random

def matriu():
    #no serveix utilitxar while x10; el problema demana utilitzar només 2 iteracions
    columnes = 0
    files = 0
    while files < 10:
        while columnes < 10:    #escriu columnes començant per 1 fins que arriba a 10
            numero_pantalla = columnes + 1 + files
            if (numero_pantalla) < 10:
                print(" ", end="")   #s'assegura que cada numero ocupi el mateix espai (afegeix un espai en els num <10 pq ocupin el mateix que num >10 )
            print(numero_pantalla, end=" ")   
            columnes+=1
        columnes = 0    #redefinim columnes pq quan arriba al final del bucle inicial és 10
        files +=1
        print("")
#matriu()

def matriu_fila(fila):
    columnes = 0
    files =  0
    while files < 10:
        while columnes < 10:    #escriu columnes començant per 1 fins que arriba a 10
            numero_pantalla = columnes + 1 + files
            if files == int(fila): #només si la fila del parametre és igual al nº de la fila imprimeix algo
                if (numero_pantalla) < 10:
                    print(" ", end="")   #s'assegura que cada numero ocupi el mateix espai (afegeix un espai en els num <10 pq ocupin el mateix que num >10 )
                print(numero_pantalla, end=" ")   
            columnes+=1
        columnes = 0
        files +=1
        print("")
#matriu_fila("2")

def joc():
    resultat = 0
    intents = 3
    partides_guanyades = 0
    partides_perdudes = 0
    intents_p = 0
    rang = [1,10]
    #menu
    while True:
        print("1. Juga")
        print("2. Estadístiques")
        print("3. Personalitza")
        print("4. Surt")
        x = int(input("Quina opció vols? "))
        if x == 1:
            resultat = random.randint(rang[0], rang[1])
            print("Estàs jugant")
            if intents_p == 0:
                intents_p = intents
            while intents > 0:
                num = int(input("Endevina el nombre: "))
                if num == resultat:
                    print("Has endevinat el número!")
                    partides_guanyades = partides_guanyades + 1
                    break
                elif num < resultat:
                    print("El resultat és un nombre més gran")
                    print(f"Intents restants {intents_p-1}")
                    intents_p = intents_p - 1
                else:
                    print("El nombre és més petit")
                    print(f"Intents restants {intents_p-1}")
                    intents_p = intents_p - 1
            if intents_p == 0:
                print("T'has quedat sense intents")
                partides_perdudes = partides_perdudes + 1
        elif x == 2:
            print(f"Partides guanyades: {partides_guanyades}")
            print(f"Partides perdudes: {partides_perdudes}")
        elif x == 3:
            print("Aquí pots personalitzar el nombre d'intents i el rang on està el nombré a endevinar.")
            intents_p = int(input("Introdueix el nombre d'intents: "))
            rang[0] = int(input("Introdueix el primer nombre del rang: "))
            rang[1] = int(input("Introdueix l'últim nombre del rang: "))

        elif x == 4:
            break
        else:
            print("La funcionalitat no existeix")

    
"""def joc():
    resultat = 0
    intents = 3
    partides_guanyades = 0
    partides_perdudes = 0
    #menu
    while True:
        print("1. Juga")
        print("2. Estadístiques")
        print("3. Surt")
        x = int(input("Quina opció vols? "))
        if x == 1:
            resultat = random.randint(1, 10)
            print("Estàs jugant")
            intents = 3
            while intents > 0:
                num = int(input("Endevina el nombre: "))
                if num == resultat:
                    print("Has endevinat el número!")
                    partides_guanyades = partides_guanyades + 1
                    break
                elif num < resultat:
                    print("El resultat és un nombre més gran")
                    print(f"Intents restants {intents-1}")
                    intents = intents - 1
                else:
                    print("El nombre és més petit")
                    print(f"Intents restants {intents-1}")
                    intents = intents - 1
            if intents == 0:
                print("T'has quedat sense intents")
                partides_perdudes = partides_perdudes + 1
        elif x == 2:
            print(f"Partides guanyades: {partides_guanyades}")
            print(f"Partides perdudes: {partides_perdudes}")
        elif x == 3:
            break
        else:
            print("La funcionalitat no existeix")"""
joc()