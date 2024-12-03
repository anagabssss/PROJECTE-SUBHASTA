# Iteracions --> repeteix en bucle fins que s'atura (while)
# break --> trenca l'últim bloc de la iteració
# continue --> trenca el bloc de codi alctual però passa al seguent
# def(paràmetre):
# #def ex1(): 
#     x = 0
#     i = 0
#     while i < 10:
#         x += int(input("Introdueix un altre numero fins al 10: "))
#         i+= 1
#     print("La mitjana és: " + str(x/10))

#funció fructifera --> 
#funció no fructifera -->

def divisors(numero): #Escriu una funció tal que donat un nombre escrigui els seus divisors
    num = numero
    while(num > 0):
        if numero % num == 0:
            print("El numero: " + str(num) + " és divisor de " + str(numero))
            num -=1

#if __name__ == "__main__": 
#divisors(10)

def ex4(): 
    """ Escriu un script tal que donats nombres fins que l’usuari introdueixi un
nombre negatiu, en calculi els seus divisors cridant a la funció anterior """
    num = 0
    while num > 0:
        divisors(num)
        num = int(input("Introdueix un nombre: "))


def ex5():
    num1 = 0
    n = 1
# Escriu un script que donats 9 enters positius, comprovi si la sèrie és creixent.
    while n <= 9:
        num2 = int(input("Introdueix un nombre: "))
        if num2 > num1: 
            num1 = num2   
        n = n+1
        print("És una serie creixent")
        else:
            print("No es una serei creixent")
"""  y = int(input("Introdueix un numero: "))
    b = y
    x = True
    i = 0
    while i < 9:
        y = int(input("Introdueix un numero: "))
        print(b, y)
        if y <= b:
            x = False
        b = y
        i = i+1
    if x == False:
        print("La serie no és creixent")
    else:
        print("La serie es creixent") """
if __name__ == "__main__": 
 ex5()

def foo():
    print("hola") #La funció foo no té el valor de "Hola"

def foo_dos(a):
    print(a)

def foo_fructifer():
    return "Hola" #La funció foo_fructifera té el valor de "Hola"

def foo_fructifer_dos(a):
    return a

if foo() == "Hola":
    print("Buenas")
else:
    print("malas") #escriurà malas --> la funció foo no és "hola"

if foo_fructifer() == "Hola":
    print("Buenas")
else: 
    print("Malas") #escriurà buenas --> la funció foo_fructifer és "hola"

"""BUCLES"""

while True:
    print("Hola") #Escriurà hola
    
while False:
    print("Hola") #no escriurà res



