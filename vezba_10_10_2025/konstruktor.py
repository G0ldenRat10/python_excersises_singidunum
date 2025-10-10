"""
Napisati program koji se sastoji od dva modula.
 
Prvi modul sadrži konstruktorsku funkciju koja predstavlja jednog studenta, čiji argumenti su ime, prezime, broj indeksa, i osvojene ocene,
a rezultat funkcije je rečnik koji predstavlja jednog studenta.
 
Modul takođe sadrži funkciju za računanje srednje ocene studenta, funkciju koja racuna najmanju ocenu,
funkciju koja racuna najvecu ocenu i funkciju za prikaz jednog studenta.
 
 
Primer prikaza jednog studenta
 
Ime:     Teodor, Prezime:    Petrovic    , Indeks:   2018201081|
Ocene: [5, 7, 6, 7, 8, 9]                                      |

"""
import math
 
def Student(ime, prezime, broj_indeksa, ocene):
    return {
        "Ime": ime,
        "Prezime": prezime,
        "Broj_Indeksa": broj_indeksa,
        "Ocene": ocene,
        }
 
def validacija_studenta(student):
    return isinstance(student, dict)
 
def srednja_ocena_studenta(student):
    if validacija_studenta(student) != True:
        print("Ovo nisu informacije o studentu.")
    else:
        ocene = student["Ocene"]
        zbir_ocena = 0
        counter = 0
        for n in ocene:
            zbir_ocena += n
            counter += 1
        formula_srednje_vrednosti = zbir_ocena / counter
        return formula_srednje_vrednosti
 
def najmanja_ocena_studenta(student):
    if validacija_studenta(student) == False:
        print("Ovo nisu informacije o studentu.")
    else:
        ocene = student["Ocene"]
        return min(ocene)

 
def najveca_ocena_studenta(student):
    if validacija_studenta(student) == False:
        print("Ovo nisu informacije o studentu.")
    else:
        ocene = student["Ocene"]
        return max(ocene)
 
def podaci_o_studentu(student):
    if validacija_studenta(student) == False:
        print("Ovo nisu informacije o studentu.")
    else:
        print(" - -" * 10)
        print("\n")
        print("{0:<10s} | {1:<10s} | {2:<6s} {3:>5d} |".format(student["Ime"], student["Prezime"],'Indeks:', student["Broj_Indeksa"]))
        print(f"\nOcene: {student['Ocene']}")
        print(f"Prosek ocena studenta: {srednja_ocena_studenta(student)}")
        print(f"Najveca ocena studenta: {najveca_ocena_studenta(student)}")
        print(f"Najmanja ocena studenta: {najmanja_ocena_studenta(student)}")
        print("\n")
        print(" - -" * 10)
