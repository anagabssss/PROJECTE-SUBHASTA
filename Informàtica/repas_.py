#terminal
#emacs document.py --> obre el document

#funcions
def foo(parametre): # --> fructifera (retorna algo a la funció)
    return parametre

foo("Hola Mundo") #dona el valor "Hola mundo" a la funció
print(foo("hola mundo")) # --> imprimeix hola mundo per pantalla


cadena = input("Dona'm algo per treure per pantalla: ") #demana un str i l'assigne a la funció
print(foo(cadena)) #imprimeix per pantalla el valor de la funció demanat per pantalla

print(type(foo(3))) # int
print(type(foo("Hola mundo"))) # str

def foo2(parametre): #--> no fructifera (no retorna res a la funció)
    print(parametre)

#doctestos
def foo(parametre):
    """
    simulació de la terminal
    python3 -m doctest -v nomfitxer.py
    >>> foo(4)
    4
    >>> foo("Hola Mundo")
    'Hola Mundo' 
    """
    return parametre

#print vs return
#print --> permet seguir el flux de programa, saber on està a cada moment
#return --> permet assignar valors


# variables
variable = 1 # nom variable = valor variable
print(variable)
variable += 1 # es pot mmodificar el valor
print(variable)
print(type(variable)) # int
variable = "Hola" # es pot modificar el tipus de variable
print(type(variable)) # str

def foo():
    variable_dos = "Adeu" # la variable només existèix dins del bloc de codi on està definida
    print(variable) # la variable de fora si que existeix dins de la funció perque la funció està dins del bloc de codi on està definida la variable

print(variable_dos) # error --> variable_dos no existeix fora de la funció on està definida


# tipus de variables

llista = ["strings", 3, 3.02, True, [1,2], {"Diccionari": "pumpum"}]

for element in llista:
    print(type(element))

bool("") # --> False
bool("Hola") # --> True
bool(" ") # --> True
bool(-2) # --> True
bool(-1) # --> True
bool(0) # --> False
bool(1) # --> True
bool(0.0) # --> False
bool(False) # --> False
bool([]) # --> False
bool([2]) # --> True
bool({}) # --> False

def no_esParell(num):
    """
    >>> no_esParell(2)
    0
    >>> no_esParell(5)
    1
    >>> no_esParell(-2)
    0
    >>> no_esParell(-5)
    -1
    >>> no_esParell(0)
    0
    """
    num_dos = num
    if num_dos > 0:
        while num_dos > 0:
            num_dos -=2
    else:
        while num_dos < 0:
            num_dos +=2
    return num_dos

bool(no_esParell(4)) # --> False --> és parell
bool(no_esParell(3)) # --> True --> no és parell

#condicionals

def esParell(num):
    """
    >>> esParell(2)
    True
    >>> esParell(5)
    False
    """
    if num % 2 == 0:
        return True
    else:
        return False
    
# bucles
def comptar(a,b):
    """
    Escriu els numeros de a a b inclosos
    >>> comptar(1,5)
    1 2 3 4 5
    >>> comptar(5,1)
    1 2 3 4 5
    """
    inici = a if a < b else b
    final = b if a < b else b
    while inici <= final:
        print(f"{inici} ", end="")
        inici += 1

comptar(1,5)


# fitxers

# touch fitxer.txt --> executa un fitxer buit (terminal)
arxiu = open("fitxer.txt", "r") #--> obre l'arxiu (mode determinat --> r)

print(arxiu.readline()) # imprimeix una linia
print(arxiu.readline()) # imprimeix la següent linia --> té un contador de quina linia ha de llegir

print(arxiu.readlines()) # imprimeix totes les linies en una llista sense codificar (llegeix des de l'última linia llegida)

for linia in arxiu:
    print(linia)

arxiu = open("fitxer.txt", "w") #--> obre en mode escriure
arxiu.write("\tEscriure\n")

arxiu.close()

arxiu = open("Fitxer.txt", "a") # --> obre en mode append --> afegeix al final del fitxer

arxiu.close()