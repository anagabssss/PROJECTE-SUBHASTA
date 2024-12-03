#lab3 - funcions i condicionals

# \n --> intro
# \t --> tab

# print("Hola", end="")
# print(", adeu")  --> escriurà els dos prints en una mateixa linia (end="" treu l'intro del final del print)

def menu():
    """Escriviu un petit programa que mostri un menú simple 
    d'una màquina expenedora, demani a l'usuari que 
    introdueixi el número corresponent a l'opció que 
    desitja, i escrigui l'acció corresponent o bé escrigui 
    un missatge d'error indicant que l'opció no és vàlida."""

    tria = 0
    plat1 = "Amanida vegetal"
    plat2 = "Pasta amb salsa bolonyesa"
    plat3 = "Plat especial del dia"
    print("1. " + plat1 + " \n2. " + plat2 + " \n3. " + plat3)
    tria = int(input("Introdueix la teva tria: "))
    if tria == 1:
        print(plat1 + " a punt!")
    elif tria == 2:
        print(plat2 + " a punt!")
    elif tria == 3:
        print(plat3 + " a punt!")
    else: 
        print("Opció incorrecta.")

#menu()

def taula_multiplicar():
    """Escriu un petit programa que demani un nombre a 
    l'usuari i escrigui la taula de multiplicar d'aquest
    nombre en ordre invers."""
    i = 10
    n = int(input("Introdueix un nombre: "))
    print("La taula de multiplicar del " + str(n) + " és: ")
    while i >= 0:
        print(str(n) + " * " + str(i) + " = " + str(n * i))
        i = i-1

#taula_multiplicar()

def factorial():
    """Escriu un petit programa que calculi el factorial 
    d'un nombre."""

    n = int(input("Introdueix un nombre: "))
    y= n
    factorial = 1
    while n > 0:
        factorial = n * factorial
        n = n-1
    print("El factorial de " + str(y) + " és " + str(factorial)) 

#factorial()

def arrel(a, b, c):
    """Escriviu un programa que calculi les arrels d'una 
    eqüació de segon grau i indiqui si tenia dues solucions 
    reals, una solució real doble o cap solució real."""

    if -4*int(b)*int(c) == 0:
        print("L'equació té una solució real doble")
    elif -4*int(b)*int(c) < 0:
        print("L'equació no té cap solució real")
    else:
        print("L'equació té dues solucions reals")

arrel(1, 1, 1)

#def matriu():


