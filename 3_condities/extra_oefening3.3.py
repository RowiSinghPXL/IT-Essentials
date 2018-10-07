waterverbruik = float(input("Geef het waterverbruik in"))



if waterverbruik < 30:
    prijs = 25
elif waterverbruik <= 200:
    prijs = 1 * waterverbruik
elif waterverbruik <= 5000:
    prijs = 1.15 * waterverbruik
else:
    prijs = 1.175  * waterverbruik


print("Het te betalen bedrag is €", prijs)


