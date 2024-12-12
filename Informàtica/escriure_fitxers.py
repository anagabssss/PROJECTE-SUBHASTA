
diccionari = {"Jan": "Duro", "Marta": "Fargas", "Roger": "Nadal"}

arxiu = open("arxiu.txt", "w")

for k, v in diccionari.items():
    arxiu.write( k +" "+ v +"\n")

arxiu.close()