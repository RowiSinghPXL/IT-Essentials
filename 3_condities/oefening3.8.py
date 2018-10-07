afstand_in_km = float(input("Geef de afstand in km: "))
klasse = int(input("Geef de klasse (1.toeristenklasse-2.charter-3.zakenreis): "))

if afstand_in_km < 1000:
    factor = 0.25
elif afstand_in_km <= 2999:
    factor = 0.20
else:
    factor = 0.12

prijs = afstand_in_km * factor

if klasse == 2:
    prijs *= 0.80
elif klasse == 3:
    prijs *= 1.3

print("Prijs is", prijs, "euro")