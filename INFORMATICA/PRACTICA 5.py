rovellons= 0
llanegues= 0
fredolics= 0
def modify_rovello (num):
    global rovellons
    rovellons += num
def modify_llanegues (num):
    global llanegues
    llanegues += num
def modify_fredolics (num):
    global fredolics
    fredolics += num

modify_fredolics (9)
modify_llanegues (55)
modify_rovello (6)

def cistella ():
    global rovellons
    global fredolics
    global llanegues
    return fredolics+llanegues+rovellons
    
print (cistella())

def mirar_cistella ():
    global rovellons
    global fredolics
    global llanegues
    if fredolics>0:
        print ("Tens "+ str(fredolics)+ " fredolics")
    else:
        print ("no tens fredolics")
        
    if llanegues>0:
        print ("Tens "+ str(llanegues) + " llanegues")
    else:
        print ("no tens llanegues")
        
    if rovellons>0:
        print ("Tens "+ str(rovellons)+ " rovellons")
    else:
        print ("no tens rovellons")
    print( "Tens " + str(cistella()) + " bolets a la cistella")
        
print(mirar_cistella())
print (rovellons)
mirar_cistella()
