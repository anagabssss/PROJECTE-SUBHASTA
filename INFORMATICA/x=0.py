def divisors(numero):
    num = numero
    while(num > 0) :
        if numero % num == 0:
            print( "El numero: " + str (num) + " és divisor de " + str( numero))
            num -= 1
#if __name__== "__main__":
divisors(10)
#Escriu un script tal que donats nombres fins que l’usuari introdueixi un nombre negatiu, en calculi els seus divisors cridant a la funció anterior
def ex4 (num):
#y=0
while y != -1:
    divisors(y)
    y=int(input("introdueix el numero per calcular el seu divisor: "))

#Escriu un script que donats 9 enters positius, comprovi si la sèrie és creixent.
y=int(input("introdueix numero: "))
b = y
x = True
while x:
    y=int(input("introdueix numero "))
    print(b,y)
 if y <=b:
        x = False
    b = y