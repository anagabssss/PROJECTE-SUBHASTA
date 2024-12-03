def compta_lletra_del_valor(diccionari):
    """
    donat un diccionari que compte claus i valors, amb l'estructura següent:
    {"clau","a"}
    ha de retornar una llista que contengui de forma ordenada quants cops surt el valor a la clau
    [1]
    >>> compta_lletra_del_valor ({"clau":"a","Belen":"e"})
    [1,2]
    """
    llista=[]
    for clau,valor in diccionari.items():
        num=0
        for lletra in clau:
            if valor == lletra:
                num +=1
        llista+=[num]
print(compta_lletra_del_valor({"clau":"a","Belen":"e"})) # [1,2] 
