def controleer_hoogte(hoogte):

    while hoogte < 2 or hoogte > 6.5:
        hoogte = int(input("Hoogte poort"))
    return hoogte

def controleer_breedte(breedte):

    while breedte < 2 or breedte > 6.5:
        breedte = int(input("Hoogte poort"))
    return breedte

def bereken_oppervlakte_poort(breedte, hoogte):
    oppervlakte = breedte * hoogte
    return oppervlakte

def bereken_gewicht_poort(oppervlakte):
    gewicht = oppervlakte * 11

    return gewicht

def bereken_prijs_poort(prijs_motor, oppervlakte, special_kleur):
    prijs_poort = oppervlakte * 113.5 + prijs_motor

    if speciale_kleur == "ja":
        prijs_poort *= 1.10
    return prijs_poort


def genereren_offertenummer(naam_verkoper, prijs):

    # totaal prijs omkeren
    prijs = str(prijs)
    lengte = len(prijs)

    offertenummer = "2018" + naam_verkoper + prijs[lengte::-1]
    return  offertenummer



naam_verkoper = input("Naam verkoper")
hoogte_poort = int(input("Hoogte poort"))
breedte_poort = int(input("Breedte poort"))
speciale_kleur = input("Special kleur")


breedte = controleer_breedte(breedte_poort)
hoogte = controleer_hoogte(hoogte_poort)
oppervlakte = bereken_oppervlakte_poort(breedte, hoogte)
gewicht = bereken_gewicht_poort(oppervlakte)


if gewicht > 300:
    motor = "X300"
    prijs_motor = 250.5
elif gewicht >= 150:
    motor = "A105"
    prijs_motor = 220.5
else:
    motor = "A101"
    prijs_motor = 120

prijs = bereken_prijs_poort(prijs_motor, oppervlakte, speciale_kleur)

print(genereren_offertenummer(naam_verkoper, prijs))

print(prijs)