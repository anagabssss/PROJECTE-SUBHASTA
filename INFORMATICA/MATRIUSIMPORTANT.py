m1=[[1,5],[4,0],[3,8]]
print(m1)
for fila in m1:
    #fila==[1,5]
    #fila ==[4,0]
    for columna in fila:
        #columna == 4
        #columna
        #columna=columna**2
        print(columna, end=" ")
    print()
#
print()
print()

for fila in range (len(m1)): 
    """
    fila == 0
    fila == 1
    ...fila==len(m1)-1
    """
    for columna in range(len(m1[fila])):
       print(m1[fila][columna],end=" ")
    print()
print()

m2=[[1,5,3],[4,0,5],[3,8,9]] #com esbrino la diagonal i els numeros que el componen??
for files in range(len(m2)):
    for columnes in range (len(m2[files])):
        if files == columnes:
            print(f"El numero {m2[files][columnes]} és dins la diagonal")# f permet afegir variables entre claudators


m3 = [[1, 5, 1],[4, 0, 3], [3, 8, 0]] 
#negar numeros de la matriu ( QUE PONGA EN NEGATIVO LOS NUMEROS)
def negar_numeros(matriu):
    m4 = []
    #llista buida per returnar
    for fila in range(len(matriu)):
        """
        m4=[] PRIMERA ITERACIO
        m4=[[-1,-5,-1]] SEGONA ITERACIO
        """
        m4==[[]] #CREEEM LLISTA BUIDA, SI NO CREEM LA LLISTA BUIDA INETNEM CACCEDIR A UNA FILA QUE JA TÉ ELEMENTS I PARAMETRES
        """
        m4=[[]] PRIMERA ITERACIO
        m4=[[-1,-5,-1],[]] SEGONA ITERACIO #EMPLENEM LLISTA
        """
        for columna in range(len(m1[fila])):
            m4[fila]+=[-matriu[fila][columna]] # AMB EL - ESTEM POSANT ELS NOMBRES EN NEGATIU
            """
            [[-1]] PRIMERA ITERACIO DE LA PRIMERA ITERACIO
            [[-1,-5]] SEGONA ITERACIO DE LA PRIMERA ITERACIO
            """
    return m4
print (negar_numeros(m3))



