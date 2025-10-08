def __main__():
    broj_automobila = int(input("Koliko automobila korisnik zeli da unese? Unesi broj: "))
    if broj_automobila < 0:
        print("\nGreska, unesi dobar broj.")
        main()
    elif broj_automobila == 0:
        print("\nProgram se gasi.")
        exit()
    else:
        lista_automobila = unos_podataka(broj_automobila)
        print(f"\nLista unesenih automobila: {lista_automobila}")
        ukupna_cena_goriva(lista_automobila)

def unos_podataka(broj_automobila):
    lista_auta = []
    for broj in range(broj_automobila):
        print(f"Uneti podatke za automobil broj {broj + 1}:")
        marka = str(input("Uneti marku automobila: ")).title()
        model = str(input("Uneti model automobila: ")).capitalize()
        predjena_kilometraza = float(input("Uneti predjenu kilometrazu auta: "))
        tip_goriva = str(input("Uneti tip goriva automobila: "))
        potrosnja = float(input("Uneti potrosnju auta: "))
        # Unos podataka u recnik:
        recnik_auta = {
            "Marka": marka,
            "Model": model,
            "Predjena_Kilometraza" : predjena_kilometraza,
            "Tip Goriva" : tip_goriva,
            "Potrosnja" : potrosnja,
            }
        # Dodatak recnika u glavnu listu:
        lista_auta.append(recnik_auta)
    return lista_auta

 

def ukupna_cena_goriva(lista_automobila):
    ukupna_cena_svih_auta = 0
    for automobil in range(len(lista_automobila)):
        auto = lista_automobila[automobil]
        marka = auto['Marka']
        model = auto['Model']
        kilometraza = auto['Predjena_Kilometraza']
        potrosnja = auto['Potrosnja']
        tip_goriva = auto['Tip Goriva']
        if tip_goriva == 'benzin':
            tip_goriva = 190
        elif tip_goriva == 'dizel':
            tip_goriva = 210
        formula = (kilometraza * potrosnja / 100) * tip_goriva
        ukupna_cena_svih_auta += formula
        print(f"\nZa auto marke {marka} i modela {model}, potrosnja goriva je {round(formula)} RSD.")
    print(f"Ukupna potrosnja goriva svih auta je {round(ukupna_cena_goriva)} RSD.")

__main__()
