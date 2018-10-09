def berekenen_lidgeld(leeftijd, aantal_kinderen, aansluitingsjaar, inkomen):
    huidig_jaar = 2018
    lidgeld = 100
    vermindering_voor_kind = aantal_kinderen * 7.5
    aantal_jaar_lid = 2018 - aansluitingsjaar

    if leeftijd > 60:
        lidgeld -= 15
    if vermindering_voor_kind < 35:
        lidgeld -= vermindering_voor_kind
    else:
        lidgeld -= 35
    if aantal_jaar_lid > 20:
        lidgeld -= 12.5
    if inkomen < 7500:
        lidgeld -= 25

    if lidgeld < 50:
        lidgeld = 50
    return  lidgeld




naam = input("Naam: ")

while naam != "X" and naam != "x":
    leeftijd = int(input("Leeftijd "))
    aantal_kinderen_ten_laste = int(input("Aantal kinderen ten laste"))
    inkomen = float(input("Inkomen jaarbasis: "))
    aansluitingsjaar = int(input("aanslutingsjaar "))

    print("Naam", naam, "lidgeld:", berekenen_lidgeld(leeftijd, aantal_kinderen_ten_laste, aansluitingsjaar, inkomen))
    naam = input("Naam: ")
