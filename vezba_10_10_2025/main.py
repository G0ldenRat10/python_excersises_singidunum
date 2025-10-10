"""
U glavnom modulu programa,
uključiti modul studenta.
Program treba da pita korisnika koliko studenata ce uneti.
Nakon toga program pita N puta da se unese neki student.
Preko adekvatne konstruktorske funkcije napraviti primerak student i
ubaciti ga u listu studenata.
 
Prikazati listu svih studenata koristeci funkciju napravljenu u modulu.
 
Prikazati srednju ocenu svih studenata.
Prikazati min ocenu za svakog studenata.
Prikazati max ocenu za svakog studenata.
 """

from konstruktor import *

def korisnicki_upit():
    try:
        odgovor_korisnika = int(input("\nUneti broj studenata koji student zeli da unese: "))
        return odgovor_korisnika
    except ValueError or TypeError:
        print("\nGreska: Unesi BROJ!")
        korisnicki_upit()
def unos_ocena():
    lista_ocena = []
    unos = True
    while unos:
        ocena = input("\nOcena (unesi 'stop' za prekid): ")
        if ocena == 'stop':
            unos = False
        elif not ocena.isdigit():
            print("Greska: Unesi broj!")
        elif ocena.isdigit() == True:
            lista_ocena.append(int(ocena))
    return lista_ocena
    
# Main
for n in range(korisnicki_upit()):
    print("\n")
    print(" - -" * 10)
    print(f"\nUnos podataka za studenta broj: {n + 1}")
    ime = str(input("\nIme: ")).title()
    prezime = str(input("\nPrezime: ")).title()
    broj_indeksa = int(input("\nBroj indeksa: "))
    ocene = unos_ocena()
     
    student = Student(ime, prezime, broj_indeksa, ocene)
    podaci_o_studentu(student)
    
            
        
    

    
