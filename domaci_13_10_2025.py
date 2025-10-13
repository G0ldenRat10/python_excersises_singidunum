# Zadatak:
# Lista, Skup

# Primeniti: INSERT SORT, SELECT SORT, BUBBLE SORT
# Uporediti: KREIRANJE LISTE, BRISANJE ELEMENATA IZ LISTE, KREIRANJE SKUPA, BRISANJE ELEMENATA IZ SKUPA

import random
import time

# Korisnicki unos za duzinu:

duzina_liste = int(input("\nUneti zeljenu duzinu liste: "))
duzina_skupa = int(input("Uneti zeljenju duzinu skupa: "))

# Kreiranje LISTE i kreiranje SKUPA:

# Lista:
start = time.time()
lista = []
for n in range(duzina_liste):
    lista.append(n)
end = time.time()
print(f"\nDuzina kreiranja liste: {round(end - start, 4)}s")

# Skup:
start = time.time()
skup = set()
for n in range(duzina_skupa):
    skup.add(n)
end = time.time()
print(f"\nDuzina kreiranja skupa: {round(end - start, 4)}s")


# Brisanje ELEMENATA IZ LISTE, Brisanje ELEMENATA IZ SKUPA:

# Korisnicki unos:
brisanje_iz_liste = int(input("\nUneti broj koji zelis da obrises iz liste: "))
brisanje_iz_skupa = int(input("Uneti broj koji zelis da obrises iz skupa: "))

# Lista:
start = time.time()
if brisanje_iz_liste in lista:
    lista.remove(brisanje_iz_liste)
else:
    print("Greska, taj broj ne pripada listi.")
end = time.time()
print(f"\nDuzina brisanja broja iz liste: {round(end - start, 4)}s")

# Skup:
start = time.time()
if brisanje_iz_skupa in skup:
    skup.remove(brisanje_iz_skupa)
else:
    print("Greska, taj broj ne pripada listi.")
end = time.time()
print(f"\nDuzina brisanja broja iz skupa: {round(end - start, 4)}s")

# Primene SORTIRANJA:

# Mesanje elemenata unutar LISTE i SKUPA:

# Lista:
random.shuffle(lista)

#Skup:                        
lista_skupa = list(skup)      #(Potrebno je vratiti ga u listu zbog randoma, potom ponovo u set kasnije)
random.shuffle(lista_skupa)

# SELECTION SORT:

def selection_sort(skup_podataka):
    start = time.time()
    for i in range(len(skup_podataka) -1):
        tekuciMin = skup_podataka[i]
        tekuciMinInd = i
        for j in range(i + 1, len(skup_podataka)):
            if tekuciMin > skup_podataka[j]:
                tekuciMin = skup_podataka[j]
                tekuciMinInd = j
        if tekuciMinInd != i:
            skup_podataka[tekuciMinInd] = skup_podataka[i]
            skup_podataka[i] = tekuciMin
    end = time.time()
    vreme = round(end - start, 4)
    print(f"\nVreme izvrsavanja SELECTION SORT-a je: {vreme}s")
        
# Izvrsavanje:
while True:
    korisnicki_odgovor = str(input("\nCega zelite da proverite brzinu? (S - Skup / L - Lista): ")).capitalize()
    if korisnicki_odgovor == 'L':
        selection_sort(lista)
        break
    elif korisnicki_odgovor == 'S':
        selection_sort(lista_skupa)
        break
    else:
        print("Pogresan odgovor! Unesi ponovo.")

# INSERTION SORT:

def insertion_sort(skup_podataka):
    start = time.time()
    for i in range(1, len(skup_podataka)):
        tekuciElement = skup_podataka[i]
        k = i - 1
        while k >= 0 and skup_podataka[k] > tekuciElement:
            skup_podataka[k+1] = skup_podataka[k]
            k = k - 1
        skup_podataka[k+1] = tekuciElement
    end = time.time()
    vreme = round(end - start, 4)
    print(f"\nVreme izvrsavanja INSERTION SORT-a je: {vreme}s")

# Izvrsavanje:
while True:
    korisnicki_odgovor = str(input("\nCega zelite da proverite brzinu? (S - Skup / L - Lista): ")).capitalize()
    if korisnicki_odgovor == 'L':
        insertion_sort(lista)
        break
    elif korisnicki_odgovor == 'S':
        insertion_sort(lista_skupa)
        break
    else:
        print("\nPogresan odgovor! Unesi ponovo.")


def bubble_sort(skup_podataka):
    start = time.time()
    n = len(skup_podataka)
    for i in range(n):
        for j in range(0, n - i - 1):
            if skup_podataka[j] > skup_podataka[j + 1]:
                skup_podataka[j], skup_podataka[j + 1] = skup_podataka[j + 1], skup_podataka[j]
    end = time.time()
    vreme = round(end - start, 4)
    print(f"\nVreme izvrsavanja BUBBLE SORT-a je: {vreme}s")

# Izvrsavanje:
while True:
    korisnicki_odgovor = str(input("\nCega zelite da proverite brzinu? (S - Skup / L - Lista): ")).capitalize()
    if korisnicki_odgovor == 'L':
        bubble_sort(lista)
        break
    elif korisnicki_odgovor == 'S':
        bubble_sort(lista_skupa)
        break
    else:
        print("\nPogresan odgovor! Unesi ponovo.")
        
# Izlazak iz programa:
exit()





