#deze oef is niet aangeraden om met een while loop te maken
aantal_studenten = 0 #aantal_studenten
totale_leeftijd = 0
aantal_leerlingen = int(input("Geef het aantal leerlingen dat in de klas zitten: "))

while(aantal_studenten < aantal_leerlingen):
    leeftijd = int(input("Geef de leeftijd van de leerling: "))
    totale_leeftijd += leeftijd #de lopende som
    aantal_studenten += 1 # Het waar of het onwaar maken van de conditie moet meestal gebeuren als laatste zin van je while blok !

gemiddelde_leeftijd = totale_leeftijd / aantal_leerlingen
print("De gemiddelde leeftijd van deze", aantal_leerlingen, "is", gemiddelde_leeftijd)


