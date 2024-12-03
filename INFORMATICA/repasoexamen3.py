
###LLISTES
#1
def sumaDeElements(llista):
    """
    Aquesta funció pren una llista de nombres i retorna la suma de tots els elements de la llista utilitzant el bucle for.
    >>> sumaDeElements([1, 2, 3, 4])
    10
    >>> sumaDeElements([10, -2, 3.5])
    11.5
    """
    suma = 0
    for nombre in llista:
        suma += nombre
    return suma

######
#2
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
        llista_inversa.append(llista[i])
    return llista_inversa
#3
def trobaMaxim(llista):
    """
    Aquesta funció pren una llista de nombres i retorna el valor màxim de la llista utilitzant el bucle for.
    
    >>> trobaMaxim([1, 2, 3, 4])
    4
    >>> trobaMaxim([10, -2, 3.5])
    10
    """
    max_num = llista[0]
    for numero in llista:
        if numero > max_num:
            max_num = numero
    return max_num
#4
def comptaElements(llista, objecte):
    """
    Aquesta funció pren una llista i un element, i retorna el nombre de vegades que l'element apareix a la llista utilitzant el bucle for.
    
    >>> comptaElements([1, 2, 3, 4, 2], 2)
    2
    >>> comptaElements(['a', 'b', 'a', 'c'], 'a')
    2
    """
    elementsiguals=0
    for element in llista:
        if element==objecte:
            elementsiguals+=1
    return elementsiguals
#4
def treuDuplicats(llista):
    """
    Aquesta funció pren una llista i retorna una nova llista amb els elements duplicats eliminats utilitzant el bucle for.
    
    >>> treuDuplicats([1, 2, 3, 4, 2, 3])
    [1, 2, 3, 4]
    >>> treuDuplicats(['a', 'b', 'a', 'c'])
    ['a', 'b', 'c']
    """
    no_duplicats=[]
    for element in llista:
        if element not in no_duplicats:
            no_duplicats.append(element)
    return no_duplicats
print(treuDuplicats([1,2,3,4,2]))

#### STRINGS
##
def lletres_comunes(str1,str2):
    """
    Donades dues cadenes de caràcters, retorna un string amb les lletres que apareixen en ambdues cadenes. utilitzant el bucle for.
    >>> lletres_comunes("hola","adeu")
    'a'
    >>> lletres_comunes("hola","hola")
    'hola'
    >>> lletres_comunes("hola","hol")
    'hol'
    >>> lletres_comunes("hola","menys")
    ''
    """
    ll_comunes = ""
    for lletra in str1:
        if lletra in str2:
            ll_comunes+=lletra
    return ll_comunes
###

def lletres_no_comunes(str1,str2):
    """
    Donades dues cadenes de caràcters, retorna una cadena amb les lletres que apareixen en una de les dues cadenes però no en les dues. utilitzant el bucle for.
    >>> lletres_no_comunes("hola","adeu")
    'hdeu'
    >>> lletres_no_comunes("hola","hola")
    ''
    """
    ll_no_comunes = ""
    for lletra in str1:
        if lletra not in str2 and lletra not in ll_no_comunes:
            ll_no_comunes += lletra
    
    for lletra in str2:
        if lletra not in str1 and lletra not in ll_no_comunes:
            ll_no_comunes += lletra
    return ll_no_comunes
####
def treu_vocals(cadena):
    """
    Donada una cadena de caràcters, retorna una cadena on s'han eliminat les vocals. Utilitzant el bucle for.

    >>> treu_vocals("hola")
    'hl'
    >>> treu_vocals("aeiou")
    ''
    """
    cadena_no_vocals = ""
    for lletra in cadena:
        if lletra.lower() not in "aeiou":
            cadena_no_vocals += lletra
    return cadena_no_vocals

def no_vocals(cadena):
    cadena_no_vocals =""
    for lletra in cadena:
        if lletra in "aeiou":
            pass
        else:
            cadena_no_vocals += lletra
    return cadena_no_vocals

def es_palindrom(cadena):
    """
    Donada una cadena de caràcters, retorna True si és un palíndrom i False en cas contrari. Utilitzant el bucle for.

    >>> es_palindrom("anna")
    True
    >>> es_palindrom("roma")
    False
    """
    for i in range(len(cadena)//2):
        if cadena[i].lower() != cadena[-i-1].lower():
            return False
    return True
