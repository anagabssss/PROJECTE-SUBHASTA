#Llistes [,] --> type 'list'
#len(-1) --> comença pel final

"""
fruites = ["pomes", "fruites"]
fruites[0] #--> "pomes"
for fruita in fruites:
    print(fruita) #--> escriu tots els elements de la llista

fruites += "peres" #--> fruites = ["pomes", "pomes", "p", "e", "r", "e" "s"]
fruites += ["peres"] #--> fruites = ["pomes", "pomes", "p", "e", "r", "e" "s", "peres"]

llista = [[1,2,3],[1,4,5]]

for element in llista:
    print(element) # escriu les files de la matriu una per una

for element in llista:
    for numero in element:
        print(numero) # escriu un per un els nombres de la matriu

llista += [[3,4,5], [9,9,9]]

llista[:2] #escriu els dos primers elements de la llista

llista_dos = ["hola", "adeu"]
llista_dos[0][0] # primer element del primer element --> "h"
llista_dos[0][1] #segon element del primer element --> "o"

llista_tres = [0,1,2]
llista_tres = [1] # --> 1
len(llista) # --> 3

fruites = ["pomes", "peres", "castanyes"]
len(fruites) #--> 3

#range --> retorna la llista de nombres des de zero fins a un menys que el paràmetre. return list 
#list(range(len(a))) # --> crea una llista amb els index de la llista (pots accedir a la ubicació dels paràmetres de la llista a)
range(3) # crea un generador de una lista
for i in range(3):
    print(i)

for i in range(len(fruites)):
    fruites[i-1] # --> "castanyes, "pomes, "peres"

#enumerate --> permet obtenir cada valor de llista i la posició que ocupen en la llista.
for i,e in enumerate(fruites):
    print(i,e) # --> 0 pomes    1 peres     2 castanyes (i -> posició de l'element) (e -> element)

cadena = "pere"
for i,e in enumerate(cadena): 
    print(i,e) # --> 0 p    1 e     2 r     3 e 

llista = [[0, "pomes"], [1, "peres"], ["2, castanyes"]]
for element in llista: # explicació de enumerate 
    print(element[0], element[1]) # --> 0 pomes     1 peres     2 castanyes (per l'element d'una llista escriu el primer element i el segon)

estudiants = ["Xavies", "Maria", "Ismael", "Marta", "Ana"]
for estudiant in estudiants:
    print(estudiant) # --> escriu tots els elements de la llista

for estudiant in estudiants:
    print("El profe ensenya a: ", estudiant)

len(estudiants) # --> 5

for i in range(len(estudiants)):
    print(i) # 0    1   2   3   4   

estudiant[0] = "Andrea" # --> ["Andrea", "Maria", "Ismael", "Marta", "Ana"]

fruites = ["pomes", "peres", "castanyes"]
fruites += ["cirera"] # fruites = ["pomes", "peres", "castanyes", "cirera"]
fruites[2:] = ["mango", "albercoc"] # fruites = ["pomes", "peres", "mango", "albercoc"]

#operacions amb llistes
fruites = ["pomes", "peres", "mango", "albercoc"]
carbohidrats = ["pasta", "arros"]
fruites + carbohidrats # ["pomes", "peres", "mango", "albercoc", "pasta", "arros"]

x = list() #--> x = []
bool(x) # --> False
dir(x) #--> mostra les operacions possibles per una variable

#.index() --> retorna la posició de l'element a la llista
["coses", 0,1].index(0) # --> 1
["coses", 0,1].index("coses") # --> 0
["coses", 0,1].index(1) # --> 2

#.reverse() --> inverteix la llista. Han de ser int
a = [1,2,3]
a.reverse() # --> [3,2,1]

#.sort() --> ordena la llista. Han de ser int
b = [4,2,3]
b.sort() # --> [2,3,4]
c = ["b", "a", 0] # --> [0, "a", "b"]
c.sort() # --> [0, "a", "b"]

#.insert(pos,element) --> afegeix l'element a la posició
fruites.insert(0, "mango") # fruites --> ["mango", "pomes", "peres", "mango", "albercoc"]

def foo(llista):
    for element in llista:
        element = element**2

def foo(llista):
    for element in range(len(llista)):
        llista[element] = llista[element]**2

def quardats_llistes(llista):
    llista_cpy = []
    for numero in llista:
        llista_cpy.append(numero**2) #.append afegeix el numero() a la llista
    return llista_cpy

#exercicis de llistes
"""
def llista_inversa():
    """Script que demani a l’usuari 10 enters i mostrar-los en ordre invers a com s’han introduït sense utilitzar-la)"""
    llista = list(input("Introdueix 10 enters: "))
    llista_inversa = []
    llargada = len(llista)
    
    #llista = [int(input("Introdueix un numero: ")) for numero in range(10)]
    llista += [int(input("Introdueix un numero: "))]
    print(llista)

    for numero in range(len(llista)):
        llista[numero] = llista_inversa[-1-numero]
        print(llista)
