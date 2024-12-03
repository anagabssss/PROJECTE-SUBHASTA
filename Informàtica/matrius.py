#matrius

def multiplica(a,b):
    """
    
    """
    c = [] #matriu resultant
    for fila in range(len(a)):
        suma = 0
        c.append([])
        for columnes_b in range(len(b[0])):
            for files_b in range(len(b)):
                suma += a[fila][files_b] * b[files_b][columnes_b]
                print(f"Multiplica {a[fila][files_b]} per {b[files_b][columnes_b]}")
                print("Següent element")
            c[fila].append(suma)
            suma = 0
    return c

multiplica([[1, 2], [3, 4]], [[9, 8], [6, 7]])


