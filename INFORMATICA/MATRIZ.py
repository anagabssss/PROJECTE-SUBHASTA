def matriu():
    columnes =0
    files = 0
    while files < 10:
        while columnes<10:
            numero_pantalla=columnes + 1 + files
            if (numero_pantalla)<10:
                print (" ", end="")
            print(numero_pantalla, end=" ")
            columnes+=1
            #12345678910
        columnes=0
        files+=1
        print(" ")
matriu()