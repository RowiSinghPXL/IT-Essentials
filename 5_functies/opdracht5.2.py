def teken_lijn(aantal, tekens):
    for i in range(aantal):
        print(tekens, end=" ")
    print()

def teken_rechthoek(aantal, hoogte, tekens):
    for i in range(hoogte):
        teken_lijn(aantal, tekens)


tekens = input("Geef een teken")
aantal = int(input("Geef het aantal"))
hoogte = int(input("Geef de hoogte"))

teken_rechthoek(aantal, hoogte, tekens)



