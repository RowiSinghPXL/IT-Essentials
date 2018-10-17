naam = input("Naam: ")
voornaam = input("Voornaam: ")

nieuwe_naam = voornaam[0].upper() + ". " + naam[0].upper() + naam[1:]
print(nieuwe_naam)