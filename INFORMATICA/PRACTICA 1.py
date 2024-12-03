a=23
b=2.3
print (a*b)
print (str(a*b))
print (a/b)
c=27
d=87
print (c//d)
print (c/d)
print (type (b))
print (type (c))
print (type ("ana"))
print (bool (3==4))
print (bool ("patata==patata"))
print ("Lectura com a paraules")

P = 4//3
print (P)
p=3/4
print(type(p))

age=3
if age < 18:
    print ("menor")
elif age < 60:
    print ("adulto")
else:
    print ("mayor")

import math
print(math.sqrt(16)) 


def comprovaPositiu(r):
    if r>0: 
        print ("Es positiu")
    else:
        print ("Es negatiu o zero")
def comprovaParell(r):
    if r%2==0:
        print ("Nombre parell")
    else:
        print ("Nombre senar")
        
comprovaParell (5)
comprovaPositiu (-8)
comprovaParell (9)