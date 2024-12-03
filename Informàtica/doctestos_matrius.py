def sumaDiagonal(m):
    """
    Donada una matriu suma la seva diagonal
    >> sumaDiagonalPrincipal([[1.0, 2.0, 3.0], [3.0, 3.0, 3.0], [7.0, 8.0, 9.0]])
    13.0
    """
    suma = 0
    for i in range(len(m)):
        suma = suma + m[i][i]
    return suma
    

def esSimetrica(m):
    """
    Retorna True o false sí només sí la matriu és simetrica
    >> esSimetrica([[1.0, 2.0, 3.0], [2.0, 2.0, 4.0], [3.0, 4.0, 3.0]])
    True
    >> esSimetrica([[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [3.0, 3.0, 3.0]])
    False
    """
    # Comprovar si la matriu és simetrica
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]!= m[j][i]:
                return False
    return True


def sumaDiagonalSecundaria(m):
    """
    Suma la diagonal inversa de la matriu
    >> sumaDiagonalSecundaria([[1.0, 2.0, 3.0], [3.0, 3.0, 3.0], [7.0, 8.0, 9.0]])
    13.0
    """
    suma = 0
    for i in range(len(m)-1, -1, -1):
        suma = suma + m[i][i]
    return suma

def sumaCantonades(m):
   """
   Suma les cantonades de una matriu
   >> cantonades([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
   8.0
   >> cantonades([[0.0, 2.0, 0.0], [1.0, 2.0, 3.0], [0.0, 9.0, 3.0]])
   3.0
   """
   # Sumar les cantonades de la matriu
   suma = 0
   for i in range(len(m)):
       suma += m[i][0] + m[i][len(m[0])-1]
   return suma

def ordreMatriu1(m):
    """
    producte de les dimensions de la matriu
    >>> ordreMatriu1([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    9
    >>> ordreMatriu1([[1.0, 2.0], [4.0, 5.0]])
    4
    """
    return len(m) * len(m[0]) # nº files * nº columnes

def ordreMatriu(m):
    """
    >>> ordreMatriu([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    [3, 3]
    >>> ordreMatriu([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]])
    [2, 4]
    """
    ordre = []
    ordre.append(len(str(m))) # afegir a la llista el nº de files
    ordre.append(len(str(m[0]))) # afegir a la llista el nº de columnes
    return ordre

def productePossible(m, n):
    """
    Donades dues matrius M x N retorna True si les matrius es poden multiplicar.
    True si nº files de m = nº columnes n
    >>> productePossible([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    False
    >>> productePossible([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    True
    >>> productePossible([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    True
    """
    return ordreMatriu(m[0]) == ordreMatriu(n[1]) # el nº de files de la matriu m (1r nº de l'ordre de m) ha de ser igual al nº de columnes de la matriu n (2n nº de l'ordre de n)

def quantsCaràcters(m):
    """
    Donada una matriu 3x3 amb caràcters retorna una matriu on cada posició representi el nombre de caràcters en aquella posició a la matriu original.
    >>> quantsCaràcters([["a", "bb", "ccc"], ["a", "bb", "ccc"], ["a", "bb", "ccc"]])
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    >>> quantsCaràcters([["a", "bc", "dvd"], ["a", "xi", "UPC"], ["El", "profe", "info"]])
    [[1, 2, 3], [1, 2, 3], [2, 5, 4]]
    """
    matriu_caracters = []
    for fila in m:
        for columna in fila:
            matriu_caracters.append(len(columna))
    return matriu_caracters



def sumaParells(m):
    """
    donada una matriu m NxM retorni la suma dels elements parells que conté.
    >>> sumaParells([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    6
    >>> sumaParells([[2, 2, 3], [2, 2, 3], [2, 2, 9]])
    12
    >>> sumaParells([[5, 3, 5], [3, 2, 3], [4, 2, 4]])
    12
    """
    suma = 0
    for fila in m:
        for columna in m:
            if columna[0]%2 == 0:
                suma = suma + columna[0]
    return suma