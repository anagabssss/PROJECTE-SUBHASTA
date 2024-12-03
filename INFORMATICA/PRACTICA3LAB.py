def maquina ():
    a = "Amenida vegetal"
    b = "Pasta amb salsa bolonyesa"
    c = "Plat especial del dia "
    x = int(input(" Introdueix el numero corresponent al l'opció que desitja: "))
    if x == 1:
        print(a)
    elif x == 2: 
        print(b)
    elif x == 3:
        print(c)
    else :
        print ("ERROR")
#maquina()
#####
def multiplicar():
    x=int(input("Introdueix un nombre: "))
    y=10
    while y>=0:
        print (str(y)+" * "+str(x)+ " = "+str(y*x))
        y=y-1
##multiplicar()
###
def factorial ():
    x=int(input("Introdueix un nombre: "))
    f=1
    a=x
    while x>0:
        f=x*f
        x=x-1
    print("el nombre factorial de " + str(a)+ " és " + str(f))
factorial()
