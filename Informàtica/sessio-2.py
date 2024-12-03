""" x = input("Diga'm la teva edat: ")
print("La teva edat és " + x)
print("D'aqui dos anys tindrás: ", int(x)+2) #input retorna str. S'ha de transformar a int per poder sumar-li algo

type(x) # --> str
y = int(x)
type(y) # --> int
bool(x) # --> True. Quan es transforma un str a bool sera True si està ple i False si està buit

z = ""
bool(z) # --> False. z està buida.

#sessió 2

#print(n = 7) #no es pot assignar una variable dins d'un print
print(7+5) #-->12

a = "Molt "
b = "treballar "
c = "i "
d = "poc "
e = "jugar "
f = "fan "
g = "de "
h = "Jack "
i = "un "
j = "avorrit." 
print(a+b+c+d+e+f+g+h+i+j)

6*1-2 # -->4
6*(1-2) # -->-6

a = "Hola"
b = "món"
c = 87
d = 2.33145
print (a+b)
print("el resultat és: "+ str(c))
print("el resultat és: " + str(c) + " minuts (" + str(c*60) + " segons)")
print(f"El resultat és: {c} minuts ({c*60} segons)") #f dins del print abans del str formatega les variables
print("La temperatura és: " + str(d))
print(a + " " + b)
print("Hola mon")

num1 = 8
num2 = 7
print(8+7)

 def suma_mitj (num1, num2):
    suma = num1+num2
    mitjana = suma/2
    return suma, mitjana
suma_mitj(2, 2)

nom = input("Com et dius: ")
edat = input("Quants anys tens: ")
print(nom + edat) 

num = int(input("Introdueix un nombre: "))
print(num/2)"""
def digues_n_vegades(s, n):
    print(int(n)*s)

digues_n_vegades("vaca seca", 4)

def justificat_a_la_dreta(s):
    tab = 0
    tab = 70 - len(s)
    print(tab*" " + s)

justificat_a_la_dreta("jo")

