def ordreMatriu(m):
    """
    producte de les dimensions de la matriu
    >>> ordreMatriu([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    9
    >>> ordreMatriu([[1.0, 2.0], [4.0, 5.0]])
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
    ordre.append(len(m)) # afegir a la llista el nº de files
    ordre.append(len(m[0])) # afegir a la llista el nº de columnes
    return ordre

def productePossible(m, n):
    """
    Donades dues matrius M x N retorna True si les matrius es poden multiplicar.
    True si nº files de m = nº columnes n
    >>> productePossible([[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]], [[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]])
    False
    >>> productePossible([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    True
    >>> productePossible([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    True
    """
    return ordreMatriu(m[0]) == ordreMatriu(n[1]) # el nº de files de la matriu m (1r nº de l'ordre de m) ha de ser igual al nº de columnes de la matriu n (2n nº de l'ordre de n)

def quantsCaracters(m):
    """
    Donada una matriu 3x3 amb caràcters retorna una matriu on cada posició representi el nombre de caràcters en aquella posició a la matriu original.
    >>> quantsCaracters([["a", "bb", "ccc"],["a", "bb", "ccc"], ["a", "bb", "ccc"]])
    [[1, 2, 3], [1, 2, 3],[1, 2, 3]]
    >>> quantsCaracters([["a", "bc", "dvd"],["a", "xi", "UPC"], ["El", "profe", "info"]])
    [[1, 2, 3], [1, 2, 3],[2, 5, 4]]
    """
    matriu_caracters = []
    for fila in m:
        for columna in fila:
            matriu_caracters.append(len(columna))
    return matriu_caracters

def multiplicaDiagonalPrincipal(m):
    """
    >>> multiplicaDiagonalPrincipal([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    6
    >>> multiplicaDiagonalPrincipal([[2, 2, 3], [2, 2, 3], [2, 2, 9]])
    36
    >>> multiplicaDiagonalPrincipal([5, 3, 5], [3, 2, 3], [4, 2, 4]])
    40

    S'ha de multiplicar els numeros on fila == columna
    """
    multiplicacio = 1
    for i in range(len(m)):
        multiplicacio = multiplicacio * m[i][i]
    return multiplicacio

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
        for columna in fila:
            for i in range(len(columna)):
                if columna[i]%2 == 0:
                    suma = suma + columna[0]
    return suma