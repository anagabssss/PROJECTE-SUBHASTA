
def sumaDeElements(llista):
    """
    Aquesta funció pren una llista de nombres i retorna la suma de tots els elements de la llista utilitzant el bucle for.
    
    >>> sumaDeElements([1, 2, 3, 4])
    10
    >>> sumaDeElements([10, -2, 3.5])
    11.5
    """

    suma = 0
    for element in llista:
        suma += element
    return suma
print(sumaDeElements([1, 2, 3, 4]))

def reverseLlista(llista):

    """
    Aquesta funció pren una llista i retorna una nova llista amb els elements en ordre invers utilitzant el bucle for.
    
    >>> reverseLlista([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverseLlista(['a', 'b', 'c'])
    ['c', 'b', 'a']
    """
    llista_inversa = []
    for numero in range(len(llista)-1, -1, -1):
        llista_inversa.append(llista[numero])
    return llista_inversa
print(reverseLlista([1, 2, 3, 4]))

def trobaMaxim(llista):
    """
    Aquesta funció pren una llista de nombres i retorna el valor màxim de la llista utilitzant el bucle for.
    
    >>> trobaMaxim([1, 2, 3, 4])
    4
    >>> trobaMaxim([10, -2, 3.5])
    10
    """
    

def comptaElements(llista, element):
    """
    Aquesta funció pren una llista i un element, i retorna el nombre de vegades que l'element apareix a la llista utilitzant el bucle for.
    
    >>> comptaElements([1, 2, 3, 4, 2], 2)
    2
    >>> comptaElements(['a', 'b', 'a', 'c'], 'a')
    2
    """
    pass

def treuDuplicats(llista):
    """
    Aquesta funció pren una llista i retorna una nova llista amb els elements duplicats eliminats utilitzant el bucle for.
    
    >>> treuDuplicats([1, 2, 3, 4, 2, 3])
    [1, 2, 3, 4]
    >>> treuDuplicats(['a', 'b', 'a', 'c'])
    ['a', 'b', 'c']
    """
    pass