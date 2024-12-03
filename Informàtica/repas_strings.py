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
            ll_comunes += lletra
    return ll_comunes
#print(lletres_comunes("hola","hol"))

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

#print(lletres_no_comunes("hola","adeu"))

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
        if lletra not in "aeiou":
            cadena_no_vocals += lletra
    return cadena_no_vocals

print(treu_vocals("hola"))  

def es_palindrom(cadena):
    """
    Donada una cadena de caràcters, retorna True si és un palíndrom i False en cas contrari. Utilitzant el bucle for.

    >>> es_palindrom("anna")
    True
    >>> es_palindrom("roma")
    False
    """

    for i in len(cadena):
        if cadena[i] == cadena[len-1]:
            range


