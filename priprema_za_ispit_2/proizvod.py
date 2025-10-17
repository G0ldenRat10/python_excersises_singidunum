from math import sqrt
import json

def proizvodKonstruktor(naziv, proizvodjac, godina_proizvodnje, masa, materijal):
    if isProizvodValid(masa,materijal) == True:
        recnik = {
                "naziv" : naziv,
                "proizvodjac" : proizvodjac,
                "godina_proizvodnje" : godina_proizvodnje,
                "masa" : masa * 0.01,
                "materijal" : materijal,
            }
        return recnik

def isProizvodValid(masa, materijal):
    # Provera materijala:
    validni_materijali = ["DRVO", "PLASTIKA", "METAL", "DRUGI_MATERIJAL"]
    if materijal not in validni_materijali:
        print("Vrednost materijala se ne podudara sa dozvoljenim vrednostima.")
        return False
    # Provera mase:
    if masa < 0.01:
        print("Vrednost mase nije validna.")
        return False
    if masa > 0.01:
        return True

def adekvatnost(recnik):
    # Provera vrednosti k za materijal:
    k = 0
    if recnik["materijal"] == "DRVO":
        k = 0.98
    elif recnik["materijal"] == "PLASTIKA":
        k = 0.93
    elif recnik["materijal"] == "METAL":
        k = 0.21
    else:
        k = 2.12
    # Racunanje adekvatnost:
    rezultat_adekvatnosti = ((2050 - recnik["godina_proizvodnje"]) * sqrt(recnik["masa"])) / (1 - k)
    return rezultat_adekvatnosti

def formatiran(recnik):
    prikaz = "\n{0:<12s}{1:<20s}{2:<13s}{3:>16.3f}\n{4:<12s}{5:<20s}{6:<13s}{7:>16s}\n{8:}{9:<12s}{10:<20s}{11:>16.2f}\n".format("Naziv:",recnik["naziv"],"Masa:",recnik["masa"],"Proizvodjac:",recnik["proizvodjac"],"Proizvedeno:",f"{str(recnik['godina_proizvodnje'])}. godine", \
                                                   "Materijal:",recnik["materijal"].lower(),"Adekvatnost:",adekvatnost(recnik))
    return prikaz


def load(datoteka):
    lista_recnika = []
    file = open(datoteka, 'r')
    while True:
        # Prvi red
        naziv = file.readline().strip()
        if naziv == '':
            break
        # Drugi red
        proizvodjac = file.readline().strip()
        # Treci red
        godina_proizvodnje = file.read(4).strip()
        masa = file.read(4).strip()
        materijal = file.readline().strip()
        # Promena materijala u odgovarajuce vrednosti
        if materijal == 'D':
            materijal = 'DRVO'
        elif materijal == 'P':
            materijal = 'PLASTIKA'
        elif materijal == 'M':
            materijal = 'METAL'
        else:
            materijal = 'DRUGI_MATERIJAL'
        # Recnik
        recnik = proizvodKonstruktor(naziv, proizvodjac, int(godina_proizvodnje), float(masa), materijal)
        lista_recnika.append(recnik)
    file.close()
    return lista_recnika

    

    
    
        
    
