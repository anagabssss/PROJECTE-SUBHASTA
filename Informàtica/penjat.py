import string


def penjat ():
    """
    variables
    paraula_secreta: paraula que introdueix el jugador A. El jugador B l'ha d'endevinar
    paraula_codificada: paraula que es mostrarà per pantalla. Es van afegint les lletres quan s'endevinen
    oportunitats: nº d'oportunitats per endevinar la paraula
    """
    print("Benvinguts al joc del penjat")
    paraula_secreta = input("Introdueix la paraula secreta")
    paraula_secreta = paraula_secreta.lower()
    paraula_codificada = ""
    oportunitats = 15
    lletres_valides = "abcdefghijklmnopqrstuvwxyz"
    #verificar paraula_secreta
    for lletra in paraula_secreta:
        if letra in lletres_valides:
            continue
        else:
            print("La paraula introduida no es vàlida.")
    for lletra in paraula_secreta:
        paraula_codificada += "_"
    print("Anem a jugar al penjat!")
    while oportunitats > 0:
        print(f"Tens {oportunitats} oportunitats")
