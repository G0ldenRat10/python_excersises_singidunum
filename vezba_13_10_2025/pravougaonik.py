def napravi_recnik_pravougaonika(a,b):
    recnik = {
        "a": a,
        "b": b,
        "povrsina" : povrsina_pravougaonika(a,b),
        "obim" : obim_pravougaonika(a,b)
        }
    return recnik

def povrsina_pravougaonika(a,b):
    rezultat = a * b
    return rezultat

def obim_pravougaonika(a,b):
    rezultat = 2 * (a+b)
    return rezultat

def provera_operativnog_sistema():    
    uredjaj = input("Na kom si oprativnom sistemu trenutno? Unesi (Linux-L, Windows-W): ").capitalize()
    if uredjaj == 'L':
        put_fajla = "/home/zaka/Desktop/Dan_10/pravougaonici.txt"
        return put_fajla
    elif uredjaj == 'W':
        put_fajla = "C:/Users/student/Downloads/pravougaonici.txt"
        return put_fajla
    else:
        print("\nGreska: Unesi pravilnu opciju.")
        provera_operativnog_sistema()
    
    
