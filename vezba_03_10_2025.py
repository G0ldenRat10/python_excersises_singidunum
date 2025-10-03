def __main__():
    testovi = []
    print("Dobrodosao.")
    print("Koliko rezultata testova ces uneti?")
    broj_unosa = int(input("Unesi broj: "))
    info_recnik_u_listu(broj_unosa, testovi)
    prikazi_prosek_bodova(testovi)
    
def info_recnik_u_listu(broj_unosa, testovi):
    for n in range(broj_unosa):
        print(" -"*30)
        print(f"Unosite test broj {n + 1}.")
        ime_predmeta = input("Unesi ime predmeta: ").title()
        ime_studenta = input("Unesi ime studenta: ").title()
        prezime_studenta = input("Unesi prezime studenta: ").title()
        broj_indeksa = int(input("Unesi broj indeksa studenta: "))
        broj_bodova = int(input("Unesi ostvareni broj bodova na ispitu: "))

        test = {
            "ime_predmeta":ime_predmeta,
            "ime_studenta":ime_studenta,
            "prezime_studenta":prezime_studenta,
            "broj_indeksa":broj_indeksa,
            "broj_bodova":broj_bodova,
            }
        testovi.append(test)

def prikazi_prosek_bodova(testovi):
    zbir_poena = 0
    broj_testova = 0
    predmet = input("Unesi naziv predmeta da prikazes prosek bodova: ").title()
    for test in testovi:
        if test["ime_predmeta"] == predmet:
            zbir_poena += test["broj_bodova"]
            broj_testova += 1
        else:
            print(f"Trenutno nema ni jedan test koji se polagao iz predmeta {predmet}.")
            print("Program se gasi.")
            exit()
            
    odgovor = zbir_poena / broj_testova
    print(f"Prosek bodova iz predmeta {predmet} je {odgovor}.")
            
__main__()
