def reverseLlista(llista):
    """
    Aquesta funció pren una llista i retorna una nova llista amb els elements en ordre invers utilitzant el bucle for.
    >>> reverseLlista([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverseLlista(['a', 'b', 'c'])
    ['c', 'b', 'a']
    """
    llista_inversa = []
    for i in range(len(llista) - 1, -1, -1):
        print reverseLlista([1,2,3,4])