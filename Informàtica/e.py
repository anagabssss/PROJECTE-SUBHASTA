def ex5():
    num1 = 0
    n = 1
# Escriu un script que donats 9 enters positius, comprovi si la sèrie és creixent.
    while n <= 9:
        num2 = int(input("Introdueix un nombre: "))
        if num2 > num1: 
            num1 = num2   
        n = n+1
    print("És una serie creixent")