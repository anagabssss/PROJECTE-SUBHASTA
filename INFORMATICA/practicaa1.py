def demanaTemperatura():
    t =int(input("Introdueix temperatura en graus Celsius: "))
    return t
def celsius2Farenheit(t):
    resultat= ( (t * 9)/5 + 32.0)
    return resultat
temperatura= demanaTemperatura()
farenheit= celsius2Farenheit(temperatura)
def mostra(c,f):
    print ("temperatura celsius: "+ str(temperatura))
    print ("equivalent farenheit: "+ str(farenheit))
mostra(temperatura,farenheit)
