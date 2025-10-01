def sabiranje(a,b):
    return a + b
def oduzimanje(a,b):
    return a - b
def mnozenje(a,b):
    return a * b
def deljenje(a,b):
    return a // b
def kalkulacija_operacije(operacija,prvi_broj,drugi_broj):
    a = prvi_broj
    b = drugi_broj
    if operacija == '+':
        print(f"\nRezultat {a}+{b}: {sabiranje(a,b)}")
    elif operacija == '-':
        print(f"\nRezultat {a}-{b}: {oduzimanje(a,b)}")
    elif operacija == '*':
        print(f"\nRezultat {a}*{b}: {mnozenje(a,b)}")
    elif operacija == '/':
        print(f"\nRezultat {a}/{b}: {deljenje(a,b)}")
    else:
        print("Unesi odgovarajucu operaciju: +,-,*,/")
def __main__():
    prvi_broj = int(input("\nUnesi prvu cifru: "))
    operacija = input("Unesi operaciju: ")
    drugi_broj = int(input("Unesi drugu cifru: "))
    odgovor = kalkulacija_operacije(operacija,prvi_broj,drugi_broj)
    while True:
        pitanje = input("\nNastavi sa koriscenjem kalkulatora?(D/N): ").capitalize()
        if pitanje == 'D':
            __main__()
        elif pitanje == 'N':
            print("\nHvala na koriscenju.")
            exit()
        else:
            print("\nUnesi pravilnu vrednost.")

print("Kalkulator se pokrece ...")
__main__()
