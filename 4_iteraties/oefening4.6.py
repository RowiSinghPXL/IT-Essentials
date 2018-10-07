artikkelnummer = int(input("Geef het artikkelnummer in: "))
totaal_bedrag = 0

while artikkelnummer != 999:
    hoeveelheid = int(input("Geef de hoeveelheid "))
    eenheidsprijs = int(input("Geef de eenheidsprijs: "))
    prijs = hoeveelheid * eenheidsprijs
    print("artikkelnummer:", artikkelnummer, "hoeveelheid:", hoeveelheid, "eenheidsprijs:", eenheidsprijs, "bedrag:",prijs)
    totaal_bedrag += prijs
    artikkelnummer = int(input("Geef het artikkelnummer in: "))

print("Het totaal te betalen bedrag is:", totaal_bedrag)



