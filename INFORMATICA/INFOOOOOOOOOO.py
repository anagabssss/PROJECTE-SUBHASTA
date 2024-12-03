def reverseLlista(llista):
    llista_inversa = []
    for i in range(len(llista) - 1, -1, -1):
        llista_inversa.append(llista[i])
    return llista_inversa