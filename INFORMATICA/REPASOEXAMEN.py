def llistes_zero(n):
    """
    >>> llistes_zero(2)
    [0,0]
    >>> llistes_zero(0)
    []
    >>> llistes_zero(4)
    [0,0,0,0]
    """
    return [0] * n
def  matrius_zero(altura,amplada):
    """
    >>> matrius_zero(1, 1)
    [0]
    >>> matrius_zero(2, 2)
    [[0, 0], [0, 0]]
    >>> matrius_zero(1, 3)
    [[0, 0, 0]
    >>> matrius_zero(3, 1)
    [[0], [0], [0]]
    >>> matrius_zero(0, 3)
    []
    >>> matrius_zero(3, 0)

    """
llistes_to_return = []
if not altura or not amplada:
    #altura=0
    #amplada=3
   # if not bool(0) or not bool(3) 
    return llistes_to_return
for pis in range (altura):
    llistes_to_return +=[llistes_zero (amplada)]
return llistes_to_return

