import math

def industrijski_robot(np, model, gp, ssk, pee, mgsr, vppd):
    # NP - Naziv Proizvodjaca
    # Model - Model
    # GP - Godina Proizvodnje (Brojcani)
    # SSK - Stepen Slobode Kretanja (Brojacani)
    # PEE - Potrosnja Elektricne Energije (Brojcani)
    # MGSR - Maksimalni Garantovani broj sati rade (Brojcani)
    # VPPD - Vrsta Pogona pokretnih delova (3 mogucnosti: "hidraulicni pogon", "elektromotorni pogon", "magnetni linearni aktuator")
    recnik_osobina_robota = {
            "np" : np,
            "model" : model,
            "gp" : gp,
            "ssk" : ssk,
            "pee" : pee,
            "mgsr" : mgsr,
            "vppd" : vppd,
        }
    return recnik_osobina_robota
def efikasnost(recnik_modela):
    # Provera pogona:
    L = 0
    if recnik_modela["vppd"] == "HP":
        L = 1.33
    elif recnik_modela["vppd"] == "EMP":
        L = 2.00
    elif recnik_modela["vppd"] == "MLA":
        L = 1.00
    else:
        print("GRESKA: U sistemu je nepostojeca vrsta pogona!")
        
    # Formula efikasnosti:
    efikasnost = (recnik_modela["pee"] * L) / (recnik_modela["ssk"] - 2) * math.sqrt(recnik_modela["mgsr"])
    return efikasnost
    

def test_brojcanih_vrednosti_robota(gp, ssk, pee, mgsr, vppd):
    dozvoljene_vrednosti_vppd = ['hidraulicni pogon', "elektromotorni_pogon", "magnetni linearni aktuator"]
    if gp > 0 and ssk > 0 and pee > 0 and mgsr > 0 and vppd in dozvoljene_vrednosti_vppd:
        return True
    else:
        return -1

with open("/home/zaka/Desktop/priprema_za_ispit/ulaz.dat", "r") as f:
    datoteka_za_citanje = f.read()

def load(datoteka_za_citanje):
    try:
        linija = datoteka_za_citanje.splitlines()
        lista_svih_podataka = []
        for n in range(0, len(linija), 2):
            lista_jednog_podatka = []
            # Gornji podaci
            pee = float(linija[n][0:8].strip())
            mgsr = float(linija[n][8:16].strip())
            gp = float(linija[n][17:22].strip())
            np = str(linija[n][23:].strip())
            # Donji podaci
            ssk = float(linija[n+1][0:8].strip())
            vppd = str(linija[n+1][8:15].strip())
            model = str(linija[n+1][15:].strip())
            recnik_modela = industrijski_robot(np, model, gp, ssk, pee, mgsr, vppd)
            recnik_modela["efikasnost"] = round(efikasnost(recnik_modela))
            lista_svih_podataka.append(recnik_modela)
        # Sortiranje po rastu efikasnosti:
        lista_svih_podataka.sort(key= lambda x: x["efikasnost"])
        return lista_svih_podataka
    except:
        print("GRESKA: Naleteli smo na gresku prilikom rada.")
    
