#Documentació i testeig de programes
# Comentaris in line --> # (Només serveix per una linia)
# Comentaris multiline --> """ Text """ (Pots escriure varies linies)
# Testing --> introdueixes la funció i el resultat desitjat  >>> nom_funció (par1, par2) resultat

def foo(x, y):
    """
    Documentació de la funció
    Aquesta funció foo donats dos paràmetres els suma i els retorna.
    -m doctest -v Tema3.py
    """
    """
    >>> foo (3, 4)
    7
    """


    return x + y


