import random
## MATRIUS
def matriu():
    columnes =0
    files = 0
    while files < 10:
        while columnes<10:
            numero_pantalla=columnes + 1 + files
            if (numero_pantalla)<10:
                print (" ", end="")
            print(numero_pantalla, end=" ")
            columnes+=1
            #12345678910
        columnes=0
        files+=1
        print(" ")
matriu()
def joc():
    resultat = random.randint(1,10)
    intents=0
    partides_guanyades=0
    partide_perdudes=0
    #menu
    while True:
        print ("1. Juga")
        print ("2. Estadístiques")
        print ("3. Surt")
        x=int(input("Quina opció vols? "))
        if x==1:
            print("Estas jugant")
            while intents < 3:
                num = int (input ("Endevina el nombre: "))
                if num == resultat:
                    print ("Has endevinat el número! ")
                    partides_guanyades =partides_guanyades + 1
                    break
                elif num < resultat:
                    print ("El resultat és un nombre més gran")
                    print ( "intents restants + {intents}" )
                    intents = intents + 1
                else:
                    print ("el nombre és més petit")
                    intents =intents + 1
        elif x==2:
            print (partides_guanyades)
            print (partide_perdudes)
        elif x == 3:
            break
joc()