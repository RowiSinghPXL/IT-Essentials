diameter_wiel = int(input("Geef de diameter van het wiel in inches: "))
afstand = float(input("Geef de af te leggen afstand in meter: "))

omwentelingen = afstand / (diameter_wiel * 3.14 * 0.025)

print("Het wiel moet", omwentelingen, "omwentelingen maken.")
