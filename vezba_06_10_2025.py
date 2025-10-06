# Poruka: Iskreno bacio sam pogled na stack overflow za ovaj algoritam,
# ali izucio sam ga te sam ga modifikovao na svoj nacin.

import math
program_aktivan = True

def __main__():
    """ Glavna funkcija programa."""
    korisnicki_broj = int(input("Unesi broj: "))
    # Logika predpostavke da svi brojevi potencijalno mogu biti prosti:
    # 1. korak: ubacujem boolean True u listu, kako bi rezultat bio lista spremna za indeksiranje
    # Primer: korisnicki_broj = 5 --> prosti = [True, True, True, True, True, True]
    potencijalno_prosti = [True] * (korisnicki_broj + 1)
    # 2. korak: obelezavanje ociglednih brojeva,
    potencijalno_prosti[0] = False; potencijalno_prosti[1] = False
    # 3. korak, formiranje lista prostih i slozenih brojeva:
    prosti_brojevi = eratostenovo_sito(korisnicki_broj, potencijalno_prosti)
    # Rezultat:
    print(f"Prosti brojevi manji od {korisnicki_broj}: {pravljenje_liste(korisnicki_broj, prosti_brojevi, trazena_lista='prosti')}")
    print(f"Slozeni brojevi manji od {korisnicki_broj}: {pravljenje_liste(korisnicki_broj, prosti_brojevi, trazena_lista='slozeni')}")
    
    
def eratostenovo_sito(korisnicki_broj, potencijalno_prosti):
    """Kalkulacija slozenih i prostih brojeva"""
    # Primenjuje se logika da je od svakog trazenog broja,
    # dovoljno proveriti sve brojeve koji su manji ili jednaki korenu tog trazenog broja,
    # i tako mozemo zakljuciti da li je broj prost ili ne.
    
    for n in range(2, int(math.sqrt(korisnicki_broj)) + 1):  # Mogao sam i: int(korisnicki_broj ** 0.5) + 1, ali sam ubacio math zbog jasnoce
        if potencijalno_prosti[n]:
            for slozeni_broj in range(n*n, korisnicki_broj + 1, n):    # Svi manji brojevi od n*n su vec visekratnici
                potencijalno_prosti[slozeni_broj] = False   # Oznacavamo brojeve koje smo zakljucili da nisu prosti vec slozeni.
    # Finalno lista sadrzi, True i False na dobrim pozicijama, te vise ne sadrzi "potencijalno proste" brojeve.
    prosti_brojevi = potencijalno_prosti
    return prosti_brojevi

def pravljenje_liste(korisnicki_broj, prosti_brojevi, trazena_lista):
    """Pravi spremne liste za rezultat"""
    # Prvo pravim prazne liste
    lista_prostih_brojeva = []
    lista_slozenih_brojeva = []
    # Proveravam u spremnoj listi sa True i False izborima, i razdvajam pojedinacno u nove liste:
    for n in range(2, korisnicki_broj):
        if prosti_brojevi[n] == True:
            lista_prostih_brojeva.append(n)
        if prosti_brojevi[n] == False:
            lista_slozenih_brojeva.append(n)
    # U zavisnosti od izabranog argumenta trazna_lista vracam potrebno:
    if trazena_lista == 'prosti':
        return lista_prostih_brojeva
    elif trazena_lista == 'slozeni':
        return lista_slozenih_brojeva
    else:
        print("ERROR: Nije unesen dobar argument koje je trazen u: trazena_lista=")

while program_aktivan == True:
    __main__()
    
    
    
    
