familienaam = input("Familienaam")
totaal_te_betalen_premie = 0
hoogste_premie = 0


while familienaam != "/" and familienaam != '*':
    voornaam = input("Voornaam")
    aantal_dienstjaren = int(input("dienstjaren: "))
    while aantal_dienstjaren <= 0 or aantal_dienstjaren >= 40:
        aantal_dienstjaren = int(input("dienstjaren: "))

    if aantal_dienstjaren >= 5:
        premie = aantal_dienstjaren * 25
    #testen of dienstjaren >= 5 en lijn 14 met een else lijn 18 mag met if blijven ==> premie wordt dan onnodig aangevuld.
    else:
        premie = 0

    totaal_te_betalen_premie += premie
    if hoogste_premie < premie:
        hoogste_premie = premie
    print("Familienaam:", familienaam, "Voornaam:", voornaam, "Aantal jaren dienst", aantal_dienstjaren, "Premie", premie, "euro")
    familienaam = input("Familienaam")



print("totaal", totaal_te_betalen_premie)
print("hoogste premie", hoogste_premie)
