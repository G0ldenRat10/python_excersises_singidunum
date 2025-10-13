#with open("C:/WINDOWS/SYSTEM32/config", "r") as f:
#    print(f.read())
#    f.close()

# Napraviti modul koji se zove "pravougaonik". U modulu napisati konstruktorsku funkciju pravougaonika koja
# uzima dva argumenta (stranice a i b) i vraca recnik sa podacima a i b pod kljucevima "a" i "b".
# U istom modulu napraviti jos dve funkcije za racunanje povrsine i obima pravougaonika, gde svaka funkcija
# za ulaz uzima jedan recnik automobila. U glavnom modulu programa ucitati datoteku "pravougaonici.txt", iz nje
# izvuci sve pravougaonike i staviti ih u jednu listu. Potrebno je napraviti program koji dodajte jedan po jedan
# pravougaonik napravljen pomocu konstruktorske funkcije kojoj su kao argumenti date vrednosti ucitane iz datoteke.
# U datoteci se u jednom redu nalaze velicine stranica a i b za jedan pravougaonik. Kada je izvrsen unos svih
# pravougaonika u listu, pronaci onaj pravougaonik koji ima najvecu povrsinu i njegove podatke upisite
# u fajl koji se zove "najveciPravougaonik.txt"

from pravougaonik import *

lista_pravougaonika = []

# Sklapanje zasebnih recnika unutar liste pravougaonika:
with open(provera_operativnog_sistema(), "r") as f:
    while True:
        trenutna_lista = []
        a = f.read(6).strip()
        b = f.readline().strip()
        if a == '' or b == '':
            break
        recnik_pravougaonika = napravi_recnik_pravougaonika(a=float(a),b=float(b))
        lista_pravougaonika.append(recnik_pravougaonika)

# Provera najvece povrsine:
najveca_povrsina = 0
for pravougaonik in lista_pravougaonika:
    if pravougaonik['povrsina'] > najveca_povrsina:
        najveca_povrsina = pravougaonik['povrsina']

# Pravljenje i pisanje fajla "najveci_pravougaonik.txt" :

with open("najveci_pravougaonik.txt", "a") as f:
    f.write("{0:<s} {1:<d}".format("Najveca povrsina na listi je:",round(najveca_povrsina)))



    
