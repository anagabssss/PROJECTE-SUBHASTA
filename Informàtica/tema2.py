#boleans/condicionals -->retorna true/false

#boleans
    #and --> les dues condicions han de ser certes pq retorni cert
    #or --> només una de les dues ha de ser certapq retorni cert
    #not
#var = input("str") --> Escriu a la variable el q s'introdueix per pantalla --> retorna str
#var.hasdigit --> mira si la variable té digits
#una variable només funciona dins del bloc on està definida
# variable global --> es pot accedir a tot el codi
# variable local --> es pot accedir només dins del seu bloc
#ide --> thonny < visual studio code
#import math

def exemple(usuari, clau):

    
    if usuari == "zestudiant" and clau == "zestudiant11":
        print("Usuari reconegut pel sistema")
    elif usuari != "zestudiant":
        print ("Username incorrecte")
    else:
        print ("Contrasenya incorrecta. Usuari no autoritzat")
        
def exercici2(num):
    if num ==0:
        print("zero")
    elif num%2 == 0:
        print("parell")
    else:
        print("senar")
        
def exercici3(num):
    if num == 0:
        print("zero")
    elif num>0:
        print("positiu")
    else:
        print("negatiu")
        
def exercici4(a, b, c):
    #l'arrel determina el tipus de soluci
    if (b**2) == 4*c*a:
        print('Aquesta equació té una solució doble')
    elif (b**2) > 4*c*a:
        print('Aquesta equació no té solucions reals')
    else:
        print('Aquesta equació té dues arrels')
        
        

    
    