def division():
    divisor=int(input("Entra divisor: "))
    dividend=int(input("Entra dividend: "))
    quocient = divisor/dividend
    residu = divisor%dividend
    print ( "El quocient de la divisio es: " + str (quocient) + " i el residu es: " + str (residu ))

##division()
def variables():
    print ("Lectura com a paraules")
    numero= input ("Entra un enter ")
    numero2= input("Entra un real ")
    print ("Conversio a nombres enter i a real")
    num1=int(numero)
    num2=float(numero2)
    print ("Els nombres son: " + str( num1) + "i" + str(num2) + "la suma es:" + str(num1+num2))
    print (numero)
    print (numero2)
    print ("Resultat de concatenacio de paraules"+ (numero+numero2))
##variables()
#print (int(5.6))
#print (float(5.6))
#print (float(5))
#print (type("a"))
##############

#def suma_nombres(a,b):
    #resultat=a+b
    #return resultat
#x = suma_nombres (4,8)
#print (x)
def suma_nombres(a,b):
    resultat=a+b
    print (resultat)
suma_nombres(4,8)

##
