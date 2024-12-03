rovellons = 0 #variables globals -->funcionen a tot el codi
llanegues = 0
fredolics = 0

def add_rovellons(num):
    global rovellons #crida la variable global. Avisa al codi intern que la variable rovellons esta al global (fora del codi)
    if num < 0 and rovellons <= 0:
            return
    rovellons += num

def add_llanegues(num):
    global llanegues
    llanegues += num

def add_fredolics(num):
    global fredolics
    fredolics += num

def cistella():
    global fredolics
    global llanegues
    global rovellons #global rovellons, llanegues, fredolics
    return fredolics + llanegues + rovellons

def mirar_cistella(): #no és una funció fructifera
    global fredolics, rovellons, llanegues #no fa falta per llegir variables globals
    if fredolics > 0:
        print ("Tens " + str(fredolics)+ " fredolics") #traça de programa
    else:
        print("No tens freedolics")

    if llanegues > 0:
        print("Tens " + str(llanegues)+ " llanegues")
    else:
        print("No tens llanegues")
    
    if rovellons > 0:
        print("Tens " + str(rovellons) + " rovellons")
    else:
        print("No tens rovellons")
    print("Tens " + str(cistella()) + " bolets a la cistella")



add_rovellons(-4)
add_fredolics(5)
add_llanegues(10)

mirar_cistella()
#retorna None si la funció no utilitza cap return