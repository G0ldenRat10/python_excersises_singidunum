import random

# Glavna funkcija, kroz koju se igra vraca nakon zavrsetka:
def __main__():
    print("\nDobro dosao u igru...")
    print("1..2..3..4..5..6..7..8..9..10..")
    print("\nPOGODI MOJ BROJ!")
    print("\nDa li hoces da igras sa svojim rasponom mogucih brojeva ili nasumicno generisanim?")
    print("Za korisnicki raspon unesi: K , Za nasumicno genersian raspon pocevsi od broja 1 unesi: N")
    while True:
            korisnicki_izbor = input("K - Korisnicki raspon / N - Nasumicno generisan raspon: ").capitalize()
            if korisnicki_izbor == 'K':
                try:
                    raspon = int(input("Unesi krajnu cifru: "))
                    korisnicka_igra(raspon=raspon)
                except ValueError:
                    print("\nUnesi pravilno cifru!")
                    raspon = int(input("Unesi krajnu cifru: "))
                    korisnicka_igra(raspon=raspon)
            elif korisnicki_izbor == 'N':
                nasumicna_duzina = int(random.randint(1,100))
                raspon = random.randrange(nasumicna_duzina)
                nasumicna_igra(raspon=raspon)

def korisnicka_igra(raspon):
    pokusaji = 0
    tajna_cifra = random.randint(1, raspon)
    while pokusaji < 10:
        pokusaj = int(input(f"\nUnesi broj od 1-{raspon}: "))
        if pokusaj != tajna_cifra:
            pokusaji += 1
            provera_toplo_hladno(pokusaj=pokusaj,tajna_cifra=tajna_cifra)
            print(f"\nOstali pokusaji:{int(10 - pokusaji)}")
        else:
            print(f"\nPogodio si! Broj jeste {tajna_cifra}! Iskorisceni pokusaji: {pokusaji}/10")
            ponovna_igra()

def nasumicna_igra(raspon):
    pokusaji = 0
    tajna_cifra = random.randint(1, raspon)
    while pokusaji < 10:
        pokusaj = int(input(f"\nUnesi broj od 1-{raspon}: "))
        if pokusaj != tajna_cifra:
            pokusaji += 1
            provera_toplo_hladno(pokusaj=pokusaj,tajna_cifra=tajna_cifra)
            print(f"\nOstali pokusaji:{int(10 - pokusaji)}")
        else:
            print(f"\nPogodio si! Broj jeste {tajna_cifra}! Iskorisceni pokusaji: {pokusaji}/10")
            ponovna_igra()
            
    # Kraj WHILE petlje od 10 pokusaja:
    print("\nIstrosio si sve pokusaje! Igra je gotova!")
    print(f"Broj je bio: {tajna_cifra}")
    ponovna_igra()
    
                
def provera_toplo_hladno(pokusaj, tajna_cifra):
    # Logika razlike brojeva, pretvaram uvek u pozitivan broj uz abs(),
    # tako da je svejedno da li je gore ili dole:
    razlika_brojeva = abs(pokusaj - tajna_cifra)
    if razlika_brojeva <= 5:
        print("Vruce!")
    elif razlika_brojeva <= 10:
        print("Toplo!")
    elif razlika_brojeva <= 15:
        print("Mlako.")
    elif razlika_brojeva <= 20:
        print("Hladno...")
    elif razlika_brojeva <= 25:
        print("LEDENO!")
    else:
        print("Ni na mapi nisi!")

def ponovna_igra():
    while True:
        print("\nDa li zelis da igras ponovo?")
        odgovor = input("D - Da zelim da igram ponovo! / N - Necu da igram vise!: ").capitalize()
        if odgovor == 'D':
            __main__()
        elif odgovor =='N':
            print("\nHvala na igranju!")
            exit()
        else:
            print("\nMolim Vas unesite jedan od odgovarajucih odgovora! (D/N)")
            
__main__()
