import math

# Korisnicki unosi:
tacka_a_x = int(input("Unesi vrednost kordinate tacke A na skali x: "))
tacka_a_y = int(input("Uneti vrednost kordinate tacke A na skali y: "))
tacka_b_x = int(input("Uneti vrednost kordinate tacke B na skali x: "))
tacka_b_y = int(input("Unesi vrednost kordinate tacke B na skali y: "))
tacka_c_x = int(input("Unesi vrednost kordinate tacke C na skali x: "))
tacka_c_y = int(input("Unesi vrednost kordinate tacke C na skali y: ")) 

# Provera da li tacke A i B mogu da formiraju pravougaonik:
if tacka_a_x < tacka_b_x and tacka_a_y > tacka_b_y:
    print("\nOblik sa unetim kordinatama je pravougaonog oblika.")
else:
    print("\nOblik sa unetim kordinatama X i Y nije pravougaonog oblika.")
    exit()

# Provera kordinata tacke C unutar pravougaonika koje odredjuju tacka A i B:
if not (tacka_a_x <= tacka_c_x <= tacka_b_x and tacka_b_y <= tacka_c_y <= tacka_a_y):
    print("\nTacka C nije unutar pravougaonika koje odredjuju tacka A i B.")
    exit()
else:
    if tacka_c_x == (tacka_b_x + tacka_a_x) / 2 and tacka_c_y == (tacka_a_y + tacka_b_y) / 2:
        print("\nTacka C je u samoj sredini pravougaonika koje odredjuju tacke A i B.")
    else:
        print("\nTacka C je unutar pravougaonika koje odredjuju tacka A i B.")

    # Provera pribliznosti tacki A:
    tacka_a_pitagora_a = tacka_a_x - tacka_c_x
    tacka_a_pitagora_b = tacka_a_y - tacka_c_y
    razdaljina_a = math.sqrt(tacka_a_pitagora_a**2 + tacka_a_pitagora_b**2)

    # Provera pribliznosti tacki B:
    tacka_b_pitagora_a = tacka_b_x - tacka_c_x
    tacka_b_pitagora_b = tacka_b_y - tacka_c_y
    razdaljina_b = math.sqrt(tacka_b_pitagora_a**2 + tacka_b_pitagora_b**2)

    # Rezultat:
    print(f"\nRazdaljina izmedju tacaka C i A iznosi: {round(razdaljina_a, 1)}")
    print(f"Razdaljina izmedju tacaka C i B iznosi: {round(razdaljina_b), 1}")
