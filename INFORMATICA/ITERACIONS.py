#Escriu un script que donats 9 enters positius, comprovi si la sèrie és creixent.
y=int(input("introdueix numero: "))
b = y
x = True
while x:
    y=int(input("introdueix numero "))
    print(b,y)
    if y <=b:
        x = False
    b = y
    