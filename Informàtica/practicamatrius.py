def ordreMatriu(m):
    """
    retorne l'ordre de la matriu (dimensions)
    >>> ordreMatriu([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    9

    1 2 3
    4 5 6
    7 8 9
    """
    ordre = 0
    ordre = len(m) # nº files
    ordre = ordre * len(m[0]) # nº columnes
    return ordre

def ordre_matriu(m):
    """
    retorne l'ordre de la matriu (dimensions)
    >>> ordre-matriu([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    9
    """
    ordre = []
    ordre.append(len(m))
    ordre.append(len(m[0]))
    return ordre

def productePossible(m,n):
    fila_m = len(m)
    columna_n =len(m[0])
    return fila_m == columna_n
productePossible([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1,2,3]])

def producte_possible(m, n): #utilitzan ordreMatriu
    return ordreMatriu(m[0]) == ordreMatriu(n[1])

def mTransposada(m): #canviar files per columnes
    """
    1 2 3      1 4 7
    4 5 6  --> 2 5 8
    7 8 9      3 6 9
    >>> mTransposada([[1,2,3], [4,5,6], [7,8,9]])
    [[1,4,7], [2,5,8], [3,6,9]]
    """
    transposada = []
    for i in range(len(m[0])):
        columna = []
        for fila in m:
            columna.append(fila[i])
        transposada.append(columna)
    return transposada

mTransposada([[1,2,3], [4,5,6], [7,8,9]])

def sumaDiagonal(m):
    """
    Donada una matriu suma la seva diagonal
    >>> sumaDiagonalPrincipal([[1.0, 2.0, 3.0], [3.0, 3.0, 3.0], [7.0, 8.0, 9.0]])
    13.0
    """
    suma = 0
    for i in range(len(m)):
        suma = suma + m[i][i]
    return suma
sumaDiagonal([[1.0, 2.0, 3.0], [3.0, 3.0, 3.0], [7.0, 8.0, 9.0]])

def esSimetrica(m):
    """
    Retorna True o false sí només sí la matriu és simetrica
    >>> esSimetrica([[1.0, 2.0, 3.0], [2.0, 2.0, 4.0], [3.0, 4.0, 3.0]])
    True
    >>> esSimetrica([[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [3.0, 3.0, 3.0]])
    False
    """
    #


def sumaDiagonalSecundaria(m):
    """
    Suma la diagonal inversa de la matriu
    >>> sumaDiagonalSecundaria([[1.0, 2.0, 3.0], [3.0, 3.0, 3.0], [7.0, 8.0, 9.0]])
    13.0
    """
    

def sumaCantonades(m):
   """
   Suma les cantonades de una matriu
   >>> cantonades([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
   8.0
   >>> cantonades([[0.0, 2.0, 0.0], [1.0, 2.0, 3.0], [0.0, 9.0, 3.0]])
   3.0
   """
   pass
