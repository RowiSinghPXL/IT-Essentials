PRIJS_VOLWASSENE = 11 # MET HOOFDLETTERS
prijs_kinderen = 6

aantal_volwassenen = int(input("Aantal volwassenen"))
#aantalVolwassenen = int(aantalVolwassenen) kan korter

aantal_kinderen = int(input("Aantal kinderen"))
#aantalKinderen = int(aantalKinderen)

totale_prijs = aantal_volwassenen * PRIJS_VOLWASSENE + aantal_kinderen * prijs_kinderen

print("De totale prijs is: ", totale_prijs)

