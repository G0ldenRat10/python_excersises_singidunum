from proizvod import *

datoteka='proizvodi.dat'

lista = load(datoteka)

# Filtriranje liste:

filtrirana_lista = []

for recnik in lista:
    adekvatnost_recnika = adekvatnost(recnik)
    if adekvatnost_recnika < 240:
        filtrirana_lista.append(recnik)
    else:
        continue

# .dot fajl:
with open(f"filtriran_{len(filtrirana_lista)}.dat", "w") as fajl:
    for recnik in filtrirana_lista:
        fajl.write(formatiran(recnik))
