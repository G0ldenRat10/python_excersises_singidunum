from industrijski_robot import *

with open("/home/zaka/Desktop/priprema_za_ispit/ulaz.dat", "r") as f:
    datoteka_za_citanje = f.read()
    

lista_robota = load(datoteka_za_citanje)

stara_duzina_liste = len(lista_robota)

zbir_efikasnosti = 0
broj_efikasnosti = 0
for robot in lista_robota:
    zbir_efikasnosti += robot["efikasnost"]
    broj_efikasnosti += 1
    
srednja_vrednost_efikasnosti = zbir_efikasnosti / broj_efikasnosti
efikasnost_50 = srednja_vrednost_efikasnosti * 0.5
efikasnost_150 = srednja_vrednost_efikasnosti * 1.5

# Provera raspona od 50% do 150%, i pripadnost robota u novoj listi:
for robot in lista_robota:
    if efikasnost_50 <= robot["efikasnost"] <= efikasnost_150:
        continue
    else:
        lista_robota.remove(robot)

nova_duzina_liste = len(lista_robota)

with open(f"izlaz_{stara_duzina_liste}_{nova_duzina_liste}.json", "a") as f:
    f.write(str(lista_robota))
    


    

