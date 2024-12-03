#REPASOTODO
def foo(parametre):
    return parametre
    #cadena=input("Dona'm algo per treure per pantalla: ")--> cadena dona el valor al parametre
print(foo("hola mundo"))
type(foo("hola mundo"))#----> funcio fructifera
type(foo(3))#----> funcio fructifera (int)

def foo(parametre):
   print(parametre)
print(foo("hola mundo"))

def foo(valor):
    #python3 -m doctes -v arxiu.py
    """
    >>>foo(4)
    4
    >>>foo("hola mundo") 
    'hola mundo'
    """
    return valor #return es el millor per asignar valors

#fluxe de programes
print(foo("Hola mundo"))
#VARIABLES
variable=1
variable+=1
print(variable)
type(variable)
print(type(variable))
variable="hola"
print(type(variable))

def foo():
    variable_dos= "adeu"
    #la variable solo existe dentro del bloque de la funcion, fuera del bloque no existe, no tiene ningun valor.
    # si que es pot accedir a variables de fora

#IMPORTANTE
llista = ["strings", 3 , 3.02 ,True,[1,2],{"diccionari":"pum pum"}]
for element in llista:
    print(type(element))
## exemples
bool (" ")
bool (-2)
bool(0)
bool(False)
bool([])
bool([2])
bool({})
bool({})
def noesparell(num):
    num_dos=num
    while num_dos >0:
        num_dos-=2
    return num_dos
print(bool(not bool(noesparell(4))))#-- false, es parell
bool(noesparell(3))# si devuelve -x es senar, True
##
def noesparell(num):
    """
    >>> noesparell(2)
    0
    >>> noesparell(5)
    1
    >>> noesparell(-2)
    0
    >>> noesparell(0)
    0
    """
    num_dos=num
    if num_dos >0:
        while num_dos > 0:
            num_dos-=2
    else:
        while num_dos < 0:
            num_dos+=2
    return num_dos
print(bool(not bool(noesparell(4))))#-- false, es parell
bool(noesparell(3))# si devuelve -x es senar, True
####
def esparell(num):
    """
    >>>esparell(2)
    True
    >>>esparell(3)
    False
    """
    if num % 2==0:
        return True
    else:
        return False
#BUCLES
def comptar(a,b):
    inici=a if a < b else b
    final=b if a < b else a
    while inici <= final:
        print(f"{inici} ", end="")
        inici+=1
print(comptar(1,5))
print(comptar(5,1))
#FTIXERS
#touch# et permet executar un fitxer buit
arxiu= open ("fitxer.txt")# li posem una variable per poder fer us d'aquest 
print(arxiu.readline()) # se guarda le primero una linia y despues la otra- automatico
print(arxiu.readline()) # lee desde donde te quedaste y termina de leer lo q te falta
#arxiu= open ("fitxer.txt", "r")# si no pongo nada se pone una r automatico
#arxiu= open ("fitxer.txt", "w")# escribir
#arxiu= open ("fitxer.txt", "w")
#   arxiu.write ("\tescriu\n") (\n : intro) (\t: tabulador)
#SEMPRE S'HA DE TANCAR EL ARXIU
arxiu.close()
arxiu= open ("fitxer.txt", "a")#obre en mode append---> afegeix al final de l'arxiu
for linia in arxiu:
    print(linia)
arxiu.close()
###############otro dia
diccionari={"clau":"valor","segonaclau":"valor"}
diccionari["cu"]= 5.34
diccionari["cu"]= 9
print(diccionari)
for i in diccionari.keys():
    print (i)
##########
diccionari={"clau":"valor","segonaclau":"xavi vete a tu casa","3rclau":"hola","clau":"novalor"}
def compta_lletres(diccionari,lletra):
    """
    cream una funcio que donat un diccionari i una lletra,retorni el numero de cops que surt la letra a
    tot el diccionari, es a dir, tant a les claus com als valors
    >>> compta_lletre({"clau":"valor},"o")
    1
    """
    comptador=0
    for clau,valor in diccionari.items():
        for caracter in clau:
            if caracter==lletra:
                comptador+=1
        for caracter in valor:
            if caracter ==lletra:
                comptador+=1
    return comptador
########################################################
def compta_lletra_del_valor(diccionari):
    """
    donat un diccionari que compte claus i valors, amb l'estructura següent:
    {"clau","a"}
    ha de retornar una llista que contengui de forma ordenada quants cops surt el valor a la clau
    [1]
    >>> compta_lletra_del_valor ({"clau":"a","Belen":"e"})
    [1,2]
    """
    llista=[]
    for clau,valor in diccionari.items():
        num=0
        for lletra in clau:
            if valor == lletra:
                num +=1
        llista+=[num]
print(compta_lletra_del_valor({"clau":"a","Belen":"e"})) # [1,2] 
