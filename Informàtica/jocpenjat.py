#joc penjat
from funcions_penjat import *

def jocPenjat():
    p = ""
    pocult = ""
    c = ""
    print("Benvinguts al joc del penjat")
    p = input("Introdueix la paraula secreta: ")
    p = eliminaMajuscules(p)
    if esParaulaCorrecta(p) == False:
        print("La paraula no és correcta. Torna a intentar-ho.")
        return
    netejaPantalla()
    
    oportunitats = 15
    pocult = paraulaOculta(p)

    while oportunitats > 0:
        print(f"Tens {oportunitats} oportunitats")
        print("Paraula oculta: ", pocult)
        c = input("Dona una lletra: ").lower()
        if not esLletraCorrecta(c):
            print("La lletra no és correcta. Torna a intentar-ho.")
            continue
        if hiHaLletra(p, c):
            pocult = actualitzaOculta(p, pocult, c)
            if contaOcults(pocult) == 0:
                print(f"Has endevinat la paraula. Felicitats! La paraula era: {p}")
                return
        else:
            print("La lletra no apareix a la paraula. Torna a intentar-ho.")
        oportunitats -= 1
    print(f"Has perdut. La paraula era: {p}")
jocPenjat()