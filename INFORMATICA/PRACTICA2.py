def ordreMatriu(m):
    ordre=0
    ordre=len(m)
    ordre=ordre*len(m[0])
    return ordre
#print(ordreMatriu([[1,2],[2,3],[3,5]]))
def ordre_matriu(m):
    ordre=[]
    ordre.append(len(m))
    ordre.append(len(m[0]))
    return ordre
#print(ordre_matriu([[1,2],[2,3],[3,5]]))
def producte_possible(m,n):
    fila_m=len(m)
    columna_n=(len(m[0]))
    return fila_m==columna_n
#print(producte_possible([[2,3],[3,4]],[[3,4],[5,6]]))

def mTransposada(m): #canviar files per columnes
    transposada = []
    for i in range(len(m[0])):
        columna = []
        for fila in m:
            columna.append(fila[i])
        transposada.append(columna)
    return transposada  
#print(mTransposada([[1,2,3],[4,5,6],[7,8,9]]))

def productePerCaràcter(m, k):
    return [[k * num for num in row] for row in m]

# Ejemplo de uso
m = [[1, 5, 3], [1, 9, 3], [9, 2, 3]]
k = "a"
resultado = productePerCaràcter(m, k)
print(resultado)
