aantal_afgelegde_km = float(input("Aantal afgelegde km per jaar"))
verbruik = float(input("Verbruik"))
prijsBrandstof = float(input("Prijs brandstof"))

totale_prijs = ((aantal_afgelegde_km / 100) * verbruik) * prijsBrandstof
kostprijs_per_km = totale_prijs / aantal_afgelegde_km

print("De totale prijs is: ", totale_prijs)
print("De kostprijs per km is:", kostprijs_per_km)