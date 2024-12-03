
def ordre():
    num1=int(input("Digue'm el primer nombre: " ))
    num2=int(input("Digue'm el segon nombre: " ))
    a=int(num1)
    b=int(num2)
    if (a < b):
        return a,b
    else:
        return b,a
#x=ordre()
#print (str(x))


def orden():
    num1=int(input("Digue'm el primer nombre: " ))
    num2=int(input("Digue'm el segon nombre: " ))
    a=int(num1)
    b=int(num2)
    if (a < b):
        print(str(a)+str(b))
    else:
        print(str(b)+str(a))
#orden()

def orden_1(a,b):
    if a>=b:
        return str(b) + " , " + str(a)
    else:
        return str(a) + " , " + str(b)

def orden_2():
    num1=int(input("Digue'm el primer nombre: " ))
    num2=int(input("Digue'm el segon nombre: " ))
    num3=int(input("Digue'm el tercer nombre: " ))
    a=int(num1)
    b=int(num2)
    c=int(num3)
    if min(a,b,c)==a:
        print(str(a)+" , "+str(orden_1(b,c)))
    elif min(a,b,c)==b:
        print(str(b)+" , "+str(orden_1(a,c)))
    else:
        print(str(c)+" , "+str(orden_1(a,b)))
#orden_2()
def rellotje():
    h=int(input("Introdueix les hores: "))
    m=int(input("Introdueix els minuts: "))
    s= int(input("Introdueix els segons: "))
    if h<24:
        if m<60:
            if s<59:
                print(str(h)+":"+str(m)+":"+ str(s+1))
    elif h<24:
        if m<60:
            if s==59:
                print("0"+":"+"0"+ ":" +"0")
    else:
        print("NO ÉS POSSIBLE")
rellotje()