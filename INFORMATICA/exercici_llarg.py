
# 1.1. Dissenyeu una funcio de nom ordreMatriu que, donada una matriu m de M x N, 
# retorni l’ordre de la matriu. Documenteu la funcio convenientment.

def ordreMatriu(m):
    """
    >>> ordreMatriu([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]) 
    9
    >>> ordreMatriu([[1.0, 2.0], [4.0, 5.0]]) 
    4
    """
    ordre=0
    ordre=len(m) # files
    ordre=ordre*len(m[0]) # columnes
    return ordre 


#1.2. Creeu una segona versio de l’anterior funcio per a retornar una llista de
#la forma [Files, Columnes] que contingui les dimensions de la matriu.

def ordre_matriu(m):
    """
    >>> ordreMatriu([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    [3, 3]
    >>> ordreMatriu([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]])
    [2, 4]
    """
    ordre=[]
    ordre.append(len(m)) #fila
    ordre.append(len(m[0])) #columna
    return ordre #[fila,columna]


#1.3. Utilitzant la funcio ordreMatriu, dissenyeu una funcio de nom productePossible 
# que, donades dues matrius de M x N, retorni True si aquestes matrius es poden 
# multiplicar i False en cas contrari. 

def productePossible (m,n):
    """
    >>> productePossible([[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]], [[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]])
    False
    >>> productePossible([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]],
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    True
    >>> productePossible([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    True
    """
    # Per tal que un producte sigui possible les columnes de una matriu m han 
    # de coincidir amb les files de una matriu n
    fila_m=len(m) 
    columna_n=(len(m[0]))
    return fila_m==columna_n

# 2 Dissenyeu una funcio de nom quantsCaracters que, donada una matriu m de 3x3 
# amb caracters, retorni una matriu on cada posicio representi el nombre de
# caracters en aquella posicio a la matriu original.
def quantsCaracters(m):
    """
    >>> quantsCaracters([["a", "bb", "ccc"],["a", "bb", "ccc"], ["a", "bb", "ccc"]])
    [[1, 2, 3], [1, 2, 3],[1, 2, 3]]
    >>> quantsCaracters([["a", "bc", "dvd"],["a", "xi", "UPC"], ["El", "profe", "info"]])
    [[1, 2, 3], [1, 2, 3],[2, 5, 4]]
    """
    m1=[[0,0,0],[0,0,0],[0,0,0]] #matriu que representara el nombre de caracters de la matriu original
    files=0
    for files in range(len(m)):#per cada fila pel rang de la llargaria de la matriu m
        for columnes in range(len(m[files])):
            m1[files][columnes] = len(m[files][columnes])
    return m1 


#3. Dissenyeu una funcio de nom multiplicaDiagonalPrincipal que, donada una matriu 
# quadrada m de N x N, retorni el resultat de multiplicar els nombres de la seva diagonal principal.
def multiplicaDiagonalPrincipal(m):
    """
    >>>multiplicaDiagonalPrincipal([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    6
    >>> multiplicaDiagonalPrincipal([[2, 2, 3], [2, 2, 3], [2, 2, 9]])
    36
    >>> multiplicaDiagonalPrincipal([5, 3, 5], [3, 2, 3], [4, 2, 4]])
    40
    """
    diagonal = 1 
    files = len(m) #al llarg de m, per la mida de m...
    for i in range(files):
        diagonal *= m[i][i]
    return diagonal

#4 Dissenyeu una funcio de nom sumaParells que, donada una matriu m
# de N x M, retorni la suma dels elements parells que conte
def sumaParells(m):
    """
    >>> sumaParells([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    6
    >>> sumaParells([[2, 2, 3], [2, 2, 3], [2, 2, 9]])
    12
    >>> sumaParells([5, 3, 5], [3, 2, 3], [4, 2, 4]])
    12
    """
    suma = 0 
    for fila in m: # per cada "fila" en m...
        for element in fila: # per cada "element" a fila
            if element % 2 == 0: # si això succeix(el nombre es parell)
                suma += element 
    return suma

@@@@@@@@@@@@
def doszeros(l):
   """
   Donada una llista d'enters, Indica si en la llista donada hi ha dos zeros consecutius
   """
   if len(l) < 2:
    return False
   finestra=[]
   finestra.append(l[0])
   finestra.append(l[1])
   i=2
   while i!=len(l) and finestra!=[0,0]:
    finestra.append(l[i])
    del finestra[0]
    i=i+1
   return (finestra==[0,0])