vast_bedrag = 20
gesprek_belgie = 0.12
gesprek_buitenland = 0.50
btw_percentage = 1.21

aantal_gesprekken_belgie = int(input("Geef het aantal gesprekken binnen Belgie in: "))
aantal_min_buitenland = int(input("Geef het aantal begonnen minuten naar het buitenland in: "))

totale_kost = ((aantal_gesprekken_belgie * gesprek_belgie) + (aantal_min_buitenland * gesprek_buitenland) + vast_bedrag) * btw_percentage

print("De totale prijs voor de afgelopen maand bedraagt:", totale_kost)