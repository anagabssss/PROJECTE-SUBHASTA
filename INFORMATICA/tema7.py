#TEMA 7 (21/11)
#mòduls i fitxers 
myFile = open ("nom")# obre el fitxer nom i li posa el nom file, el fitxer ha d'estar dins del mateix directori que el codi executat
#permisos per obrir r: read , w:write,r+ lectura i escriptori, a: append. afegeix al final del fitxer
#si intentes obrir un fitxer no existent amb permis W, crea el fitxer

myFile.write("Hola\n")#escriu a sobre el fitxer
print(myFile.write("sadas\n"))#escriu el nombre de lletres
myFile.read()#llegeix el document
myFile.readline()#llegeix una linia
myFile.readlines()#llegeix totes les linies
myFile.close()#sempre s'ha de tancar el fitxer

# MODULS
import sys
print (sys.argv)# cada espacio es un argumento # cada espacio serpara los argumentos formando lista
llista = sys.argv[1:] # quita lo que no sirve, lo primero porque es el nombre del documento
suma=0
for i in llista:
    suma+= float(i)
print(suma)

#EXERCICIS
import sys
def obtenirFitxer():
    nomfitxer=sys.argv[1]
    return nomfitxer
def comptaLinies(fitxer):
    """
    Compta quantes linies te un fitxer donat
    """
    xfile=open(fitxer)
    count=0
    for line in xfile:
        count+=1
        xfile.close()
    return count
def comptaparaula(fitxer,paraula):
    """
    Compta quantes vegades apareix la paraula donada dins el fitxer
    """
    xfile=open(fitxer)
    count=0
    for line in xfile:
        print (line)
        count+=line.count(paraula)
        print (count)
    return count
print (comptaparaula(obtenirFitxer(),"de"))
# DICCIONARIS (19/11)
diccionari= {"clau":"valor"} #MOLT IMPORTANT
diccionari["clau"] #--> "valor"
diccionari["clau"]=3
diccionari["clau"]=3#--> 3
#for i in diccionari.keys():#--> ... et retorna les claus del diccionari CONTINUA A LA FOTOGRAFIA
diccionari={"clau":3, "dos_clau":5}
diccionari ["clau"]#-->3
diccionari["clau_dos"]#-->5
for i in diccionari.values():
    print(i)
    #-->3-5-..
print(diccionari.keys())#-->[clau,dos_clau,..]
print( diccionari.values())#-->dict_values[3,5,9]
print (diccionari)#--> ["clau":3, "dos_clau":5, "sadsad":9]
print (list(diccionari.values()))#---> [3,5,9]
#--->les claus ha de ser mutables :strings; no llistes(diccionari té len) ;/( items; fa una llista de clau y valor)

for k,v in diccionari.items():
    print(f"la clau{k} conté el valor{v}")
    #--->La clau conté el valor 3
    #-->la clau 2 conté el valor 5
llista=["hola","adeu","joan"]
for i,e in enumerate(llista):
    print(i,e)
    #--->0hola
    #--->1 adeu
    #---> 2 joan
llista= llista(diccionari)
#import string IMPORTANT PRÀCTICAR AIXÒ
# fhand=open(’fitxer.txt’)
# counts=dict()
# for line in fhand:
# paraules=line.split()
# for paraula in paraules:
# counts[paraula]=counts.get(paraula,0)+1
# print "Diccionari"
# print counts
# llista=list()
# for clau,valor in counts.items():
# llista.append((clau,valor))
# llista.sort(reverse=True)
# print "llista ordenada"
# print llista
# for clau,valor in llista[:10]:
# print clau,valores
estudiants_notes={"ian":4,"xavier":2,...}
print (estudiants_notes)#--->ian:4...
for i,v in diccionari.items():
    print(f"L'estudiant{i}ha tret{v}")
estudiants_notes["ian"]#--->4
estudiants_notes.get("ian")#--->4
bool(estudiants_notes.get("melany"))#--->FALSE "el get hace que el porgrama no falle si no existe la "variable""
#bool(none)
#--->False
print(estudiants_notes.get("melany",0))
#--->0
####1
estudiants_notes.pop("xavier")
#--->2
print (estudiants_notes)
#---> et retornara la llista sense xavier
####1
#############2
def indica_suspes(diccionari,nota_minima,persona):
    """
   Dona't un diccionari una nota minima i el nom de la persona, indica si ha estat supes o no i si i nomes si a aprovat, la elimines del diccionari
    indica_suspes({"joel":2,"jan":6},5,"joel")
    True
    indica_suspes({"joel":2,"jan":6},5,"Jan")
    False
    """
    ###2.1
    nota=diccionari.get(persona,"NP")
    if nota == "NP":
        return False
    elif nota<nota_minima:
        return True
    else:
        return False
    ###2.2
    return diccionari.get(persona,"0") < nota_minima 
estudiants={"joel":2,"jan":6}
estudiant = input("introdueix-me el nom d'un estudiant: ")
print(indica_suspes(estudiants,5,estudiant))
###3
#Escriviu un programa anomenat aparicionsLletres.py que llegeixi una cadena donada per la línia de comandes i
#retorni una taula amb les lletres de l'abecedari per ordre alfabètic que apareguin en la cadena donada, amb 
#el nombre d'aparicions per cada lletra. Un exemple d'execució del vostre programa podria ser, donada la següent 
#entrada, el vostre programa hauria de retornar:
#$python aparicionsLletres.py "hola adeu"
# a 
# d 1
# e 1
# h 1
# l 1
# 0 1
# u 1

#### forma chatgpt
import sys
from collections import Counter

def aparicionsLletrespy():
    if len(sys.argv) != 2:
        print("Ús: python aparicionsLletres.py <cadena>")
        sys.exit(1)
    
    # Agafar la cadena des de la línia de comandes
    cadena = sys.argv[1]
    
    # Normalitzar la cadena (convertir a minúscules)
    cadena = cadena.lower()
    
    # Inicialitzar un diccionari per les lletres de l'abecedari
    lletres_abecedari = "abcdefghijklmnopqrstuvwxyz"
    comptador = Counter(c for c in cadena if c in lletres_abecedari)
    
    # Mostrar les lletres per ordre alfabètic
    print("Lletra | Aparicions")
    print("--------------------")
    for lletra in lletres_abecedari:
        print(f"{lletra}     | {comptador[lletra]}")

if __name__ == "__main__":
    main()
####FORMA MESTRE
import sys
diccionari={}
print(sys.argv[1])
for lletra in sys.argv[1]:
    if lletra == " ":
        continue
    if diccionari.get (lletra):
        diccionari[lletra]+=1
    else:
        diccionari[lletra]=1
tmp=list(diccionari.items()) #items lista de listes
tmp.sort# sort los ordena por orden alfabetico
for clau,valor in tmp:
    print(f"{clau}{valor}")

#moduls
import string
string.ascii_letters
#REPÀS TOT
arxiu=open("arxiu.txt","r")#-----> r(read),w(write)
for linia in arxiu:
    print(linia)
print(arxiu.readlines())#-----> escriu totes les linies seguides
arxiu.close()
#
arxiu = open("arxiu_dos.txt","w")#write
arxiu.write("Bon dia\n")
#cat arxiu_dos-->bon dia
#\n espacios
arxiu.close()
#nano paraules.txt&
arxiu = open("arxiu_dos.txt","r")#read
for linia in arxiu:
    for caracter in linia:#escriu un caracter per linia
        print (caracter)
    for linia in arxiu:#escriu una linia per linia
        print (f"la linia es: {linia}")
#
for linia in arxiu:
    paraula=" "
    for caracter in linia:
        if caracter == " ":
            pass
        else:
            paraula+=caracter
#
arxiu = open("arxiu_dos.txt","r")#read
diccionari= {}
for linia in arxiu:
    paraula=""
    for caracter in linia: # per cada lletra
        if caracter ==" ":#si hi ha un espai -->comenza una nova paraula
            paraula_check=paraula.lower()#passa a minuscula
            if diccionari.get(paraula_check,0):#si paraula ja esta al diccionari
                diccionari[paraula_check]+=1#suma 1 al contador de la paraula
            else:#sino esta al diccionari
                diccionari[paraula_check]=1 # afegeix el contador de la paraula a 1
            paraula="" #reinicia la variable paraula
        else:
            paraula+=caracter #afegeix la lletra a la paraula
for k,v in diccionari.items():
    print(f"la paraula{k}ha sortit {v} cops")
# items=llistes de llistes- agrupacions de cada valor
# ---> python listo los comprime
#           