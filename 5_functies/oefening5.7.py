def berekenen_boete(aantal_boeken, aantal_dagen_overschreden):
    boete = (aantal_dagen_overschreden * 0.7) * aantal_boeken
    if aantal_dagen_overschreden >= 45:
        boete += 0.84
    return boete


naam = input("Naam: ")
while naam != "xx":
    aantal_boeken = int(input("Aantal boeken: "))
    aantal_dagen_overschreden = int(input("Aantal dagen overschreden: "))
    print(naam, "zijn boete is €", berekenen_boete(aantal_dagen_overschreden,aantal_dagen_overschreden))
    naam = input("Naam: ")

