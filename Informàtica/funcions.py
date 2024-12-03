#funcions penjat

def cincLinies():
    """
    Mostra per pantalla 5 línies en blanc
    """

    print("\n"*5)

def netejaPantalla():
    """
    Mostra per pantalla 25 línies en blanc
    """

    print("\n"*25)

def eliminaMajuscules(p):
    """
    Donada una cadena p, retorna la cadena resultant de passar tot p a minúscules
    """

    return p.lower()

def esParaulaCorrecta(p):
    """
    Donada una cadena p, retorna cert si i només si tots els caràcters de p són abecedaris
    """

    return p.isalpha()

def esLletraCorrecta(c):
    """
    Donat un caràcter c, retorna cert si i només si el caràcter c és abecedari
    """
    
    return c.isalpha()

def paraulaOculta(p):
    """
    Donada una cadena p retorna la cadena resultant de reemplaçar totes les lletres de p per ’_’
    """
    pocult = ""
    for lletra in p:
        pocult += "_"
    return pocult

def hiHaLletra(p, c):
    """
    Donada una cadena p i un caràcter c, retorna cert si la lletra c és present a la paraula p
    """
    
    return c in p
    
def actualitzaOculta(p, pocult, c):
    """
    Donada una cadena p, una cadena pocult i un caràcter c, retorna la cadena resultant de 
    canviar les aparicions de la lletra c a la paraula p en la paraula pocult
    """

    return pocult.replace(c, p, pocult.count(c))

def contaOcults(p):
    """
    Donada una cadena p, retorna el nombre de caràcters ocults (’_’) que hi ha a la paraula p
    """
    
    return p.count("_")
