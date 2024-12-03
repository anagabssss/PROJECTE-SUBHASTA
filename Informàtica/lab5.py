def llistes_zero(n):
    """
    >>> llistes_zero(2)
    [0, 0]
    >>> llistes_zero(0)
    []
    >>> llistes_zero(4)
    [0, 0, 0, 0]
    -m doctest -v nom.py
    """
    return [0] * n

def matrius_zero(alcada, amplada):
    """
    >>> matrius_zero(1,1)
    [[0]]
    >>> matrius_zero(2,2)
    [[0, 0], [0, 0]]

    >>> matrius_zero(2,3)
    [[0,0,0], [0,0,0]]
    >>> matrius_zero(3,1)
    [[0], [0], [0]]
    >>> matrius_zero(0,3)
    []
    >>> matrius_zero(3,0)
    []
    """
    llista_to_return = []
    if not alcada or not amplada:
        return llista_to_return
    for pis in range(alcada):
        llista_to_return += [llistes_zero(amplada)]
    return llista_to_return

def func():
    a = int(input('Escriu un nombre: '))

    if a % 2 != 0 :

        print ('primer') 

    elif a == 3 : 

        print ('segon') 

    elif a - 5 > 0 : 

        print ('tercer') 

    else: 

        print ('quart')

func()