naam_speler = input("Naam: ")
prijs_vorig_seizoen = float(input("Prijs vorig seizoen"))
leeftijd = int(input("leeftijd"))
gemiddelde_beoordeelingscijfer = int(input("cijfer tussen 0 en 10"))
type_speler = input("Aanvaller, Middenvelder, Verdediger, Doelman")
aantal_doelpunten = int(input("Geef het aantal doelpunten"))

basisprijs = prijs_vorig_seizoen

if leeftijd < 25:
    basisprijs *= 1.1
elif leeftijd > 30:
    basisprijs *= 0.95

if type_speler == "Aanvaller":
    if aantal_doelpunten > 5:
        bonus = aantal_doelpunten - 5
        prijs = 5 * 10000 + bonus *  20000 + basisprijs
elif type_speler == "Middenvelder" or "Verdediger" or "Doelman":
    prijs = 10000 * gemiddelde_beoordeelingscijfer
    if type_speler == "Doelman" and aantal_doelpunten >= 20:
        prijs -= 9000

print("naam:", naam_speler, "prijs vorig seizoen", prijs_vorig_seizoen, "nieuwe prijs", prijs)




