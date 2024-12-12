def addProduct():

    """
    Donada una llista de productes subhastables, un
    nom de producte, una descripció i un preu de sortida, 
    afegeixi el producte a la llista.
    El producte afegit ha de ser un diccionari que contingui 
    les claus name, description i price.
    >>> products = []
    >>> addProduct(products, "Port`atil HP", "16 GB RAM, SSD 512 GB", 500)
    >>> products
    [{’name’: ’Port`atil HP’, ’description’: ’16 GB RAM, SSD 512 GB’, ’price’: 500}]
    """

def removeProduct():
    """
    Donada una llista de productes subhastables
    i l’índex d’un producte, elimini aquest producte de la llista.
    La funció ha de comprovar que l’índex proporcionat sigui vàlid 
    abans d’intentar eliminar el producte.
    >>> products = [{’name’: ’Port`atil HP’, ’description’: ’16 GB RAM’, ’price’: 500}]
    >>> removeProduct(products, 0)
    >>> products
    []
    """

def showProductsSortedByPrice():
    """
    Donada una llista de productes subhastables, mostri la informació 
    dels productes subhastables ordenats per preu de sortida en ordre 
    ascendent.
    Pista: Per ordenar una llista de diccionaris segons un camp concret, 
    com ara el preu, podeu utilitzar el mètode sort() amb el paràmetre 
    key. En lloc d’utilitzar una funció lambda, podeu definir una funció 
    que obtingui el preu d’un producte i passar aquesta funció com a 
    argument. Per exemple:

    def get_price(product):
        return product[’price’]

    products.sort(key=get_price)

    Un exemple d’ús d’aquesta funció podria ser:

    >>> products = [{’name’: ’Port`atil HP’, ’description’: ’16 GB RAM’, ’price’: 500},
    {’name’: ’Smartphone Samsung’, ’description’: ’Galaxy S21’, ’price’: 300}]
    >>> showProductsSortedByPrice(products)
    Llista de productes disponibles ordenats per preu:

    1. Smartphone Samsung - Galaxy S21 (Preu de sortida: 300)
    2. Portàtil HP - 16 GB RAM (Preu de sortida: 500)
    """

def startAuction():
    """
    Donada una llista de productes subhastables, una llista de productes 
    ja subhastats i un índex de producte, gestioni una subhasta d’aquest 
    producte.

    La funció ha de permetre als licitadors fer ofertes successives fins 
    que s’introdueixi la paraula ’fi’, moment en què la subhasta 
    finalitza i es guarda el guanyador i l’oferta final.

    El resultat de la subhasta s’ha de desar en una llista anomenada 
    auction history (amb l’històric de productes subhastats), que conté 
    el nom del producte, el guanyador i el preu final. A més, el producte 
    subhastat s’ha de treure de la llista de productes subhastables.
    Un exemple d’ús d’aquesta funció podria ser:

    >>> products = [{’name’: ’Port`atil HP’, ’description’: ’16 GB RAM’, ’price’: 500}]
    >>> auction_history = []
    >>> startAuction(products, auction_history, 0)
    Comença la subhasta per Portàtil HP!

    L’actual preu és 500. Introdueix una nova oferta o ’fi’ per finalitzar: 550
    Introdueix el nom del licitador: Maria

    L’actual preu ´es 550. Introdueix una nova oferta o ’fi’ per finalitzar: fi
    
    Subhasta finalitzada. El guanyador ´es Maria amb una oferta de 550.
    >>> auction_history
    [{’product’: ’Port`atil HP’, ’winner’: ’Maria’, ’final_price’: 550}]
    >>> products
    []

    NOTA: Assegureu-vos que, despr´es de la subhasta, el producte es 
    mogui de la llista de productes subhastables a la llista de 
    productes subhastats i que el preu final del producte actualitzat 
    sigui reflectit en aquesta llista!
    """

def showAuctionHistory():
    """
    Donada una llista de subhastes, mostri per pantalla l’historial de 
    subhastes realitzades, incloent el nom del producte, el guanyador i 
    el preu final.

    Un exemple d’ús d’aquesta funció podria ser:

    >>> auction_history = [{’product’: ’Portàtil HP’, ’winner’: ’Maria’, ’final_price’: 550}]
    >>> showAuctionHistory(auction_history)
    Historial de subhastes:

    Producte: Port`atil HP - Guanyador: Maria - Preu Final: 550
    """

def menu():
    """
    mostra el menú principal del sistema de subhastes i retorni l’opció 
    seleccionada per l’usuari.
    Un exemple d’ús d’aquesta funció podria ser:
    >>> menu()
    Menú Subhasta Virtual
    ====================
    1. Afegir productes a la subhasta.
    2. Eliminar producte de la subhasta.
    3. Veure productes de la subhasta ordenats per preu.
    4. Iniciar subhasta.
    5. Veure historial de subhastes.
    6. Sortir.

    Tria la teva opció: 1
    1
    """

#tasques opcionals

def loadProductsFromFile():
    """
    Donada una llista de productes sub-hastables i el nom d’un fitxer, 
    carregui els productes subhastables des d’aquest fitxer a la llista.
    Cada línia del fitxer conté la informacié d’un producte amb el format
    seg¨uent: nom, descripció i preu, separats per comes. La funció ha 
    d’afegir els productes a la llista de productes subhastables 
    (mantenint els productes que ja hi hagées prèviament a la llista).
    
    El fitxer ha de tenir el següent format:

    Portàtil HP,16 GB RAM,500
    Smartphone Samsung,Galaxy S21,300

    Un exemple d’ús d’aquesta funció podria ser:
    >>> products = []
    >>> loadProductsFromFile(products, "products.txt")
    >>> products
    [{’name’: ’Portàtil HP’, ’description’: ’16 GB RAM’, ’price’: 500},{’name’: ’Smartphone Samsung’, ’description’: ’Galaxy S21’, ’price’: 300}]
    NOTA: Caldrà modificar el menú i el programa principal per afegir 
    una nova opció que permeti carregar productes des d’un fitxer.
    """

def saveProductsToFile():
    """
    Donada una llista de productes subhastables i un nom de fitxer, 
    exporti els productes subhastables a aquest fitxer. Cada producte 
    s’ha de desar en una línia, amb el nom, descripció i preu separats 
    per comes.
    El fitxer generat tindrà el format següent:
    Portàtil HP,16 GB RAM,500
    Smartphone Samsung,Galaxy S21,300
    Un exemple d’ús d’aquesta funció podria ser:
    >>> products = [{’name’: ’Portàtil HP’, ’description’: ’16 GB RAM’, ’price’: 500}]
    >>> saveProductsToFile(products, "products_to_auction.txt")
    NOTA: Caldrà modificar el menú i el programa principal per afegir una
    nova opció que permeti exportar els productes subhastables a un 
    fitxer.
    """

def saveActuionHistoryToFile():
    """
    Donada una llista amb l’historial de subhastes i un nom de fitxer, 
    exporti l’històric de subhastes a aquest fitxer. Cada subhasta s’ha
    de desar en una línia, amb el nom del producte, el guanyador i el 
    preu final separats per comes.

    El fitxer generat tindrà el format següent:

    Portàtil HP,Maria,550
    Smartphone Samsung,Joan,400

    Un exemple d’ús d’aquesta funció podria ser:

    >>> auction_history = [{’product’: ’Port`atil HP’, ’winner’: ’Maria’, ’final_price’: 550}]
    >>> saveAuctionHistoryToFile(auction_history, "auction_history.txt")
    
    NOTA: Caldrà modificar el menú i el programa principal per afegir una
    nova opció que permeti exportar l’històric de subhastes a un fitxer.
    """

def modifyProductPrice():
    """
    Donada una llista de productes subhastables, un índex de producte i 
    un nou preu, actualitzi el preu de sortida d’aquest producte. 
    Aquestafunció ha de comprovar que el preu sigui positiu.

    Un exemple d’ús d’aquesta funció podria ser:

    >>> products = [{’name’: ’Port`atil HP’, ’description’: ’16 GB RAM, SSD 512 GB’, ’price’: 500}]
    >>> modifyProductPrice(products, 0, 450)
    >>> products 
    [{’name’: ’Port`atil HP’, ’description’: ’16 GB RAM, SSD 512 GB’, ’price’: 450}]
   
     NOTA: Caldrà modificar el menú i el programa principal per afegir 
    una nova opció que permeti modificar el preu d’un producte existent.
    """

def generateAuctionSummary():
    """
    donada la llista de l’historial de
    subhastes, generi un resum de les subhastes realitzades, indicant el 
    nombre total de subhastes, el preu mitjà de venda i el producte que ha
    tingut la venda més alta. La funció ha de mostrar aquest resum a 
    l’usuari.
    Un exemple d’ús d’aquesta funció podria ser:

    auction_history = [{’product’: ’Port`atil HP’, ’winner’: ’Maria’,
    ’final_price’: 550}, {’product’: ’Smartphone Samsung’, ’winner’: 
    ’Joan’, ’final_price’: 400}]
    >>> generateAuctionSummary(auction_history)
    Nombre total de subhastes: 2
    Preu mitjà de venda: 475.0
    Producte amb la venda més alta: Portàtil HP"
    NOTA: Caldrà modificar el menú i el programa principal per afegir una
    opció que permeti mostrar el resum de subhastes a l’usuari.
    """

def filterAuctionsByPrice():
    """
    Donada la llista de l’historial de subhastes i un interval de preus 
    (preu mínim i preu màxim), mostri totes les subhastes que han tingut
    un preu final dins d’aquest interval. Aquesta funció permetrà als 
    usuaris veure les subhastes que es van tancar a preus específics.
    Un exemple d’ús d’aquesta funció podria ser:
    >>> auction_history = [{’product’: ’Port`atil HP’, ’winner’: ’Maria’,
    ’final_price’: 550}, {’product’: ’Smartphone Samsung’, ’winner’: ’Joan’,
    ’final_price’: 400}, {’product’: ’Tablet Apple’, ’winner’: ’Anna’,
    ’final_price’: 300}]
    >>> filterAuctionsByPrice(auction_history, 300, 500)
    Producte: Smartphone Samsung, Guanyador: Joan, Preu final: 400
    Producte: Tablet Apple, Guanyador: Anna, Preu final: 300
    
    NOTA: Caldrà modificar el menú i el programa principal per afegir 
    una opció que permeti filtrar les subhastes segons un interval de 
    preus.
    """