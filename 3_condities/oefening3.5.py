BTW_PERCENTAGE = 0.21
EENHEIDSPRIJS = 11.50

hoeveelheid_artikels = int(input("Hoeveel artikels"))

totale_prijs = hoeveelheid_artikels * 11.50 * 0.21

if totale_prijs > 1000:
    totale_prijs *= 0.90

print("Het totale bedrag dat de klan moet betalen is", totale_prijs)
