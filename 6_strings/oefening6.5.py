def bereken_prijs_per_persoon(aantal_sterren, hotelcode):
    if hotelcode[:2] == "HI":
        prijs = 70
    elif aantal_sterren >= 4 or hotelcode[:2] == "AN" or hotelcode[:2] == "BR":
        prijs =  60
    elif aantal_sterren == 3:
        prijs =  56
    else:
        prijs =   48

    return prijs
def bereken_prijs_per_kind(aantal_kinderen, kindercode, aantal_sterren, hotelcode):
    volwassene_prijs = bereken_prijs_per_persoon(aantal_sterren,hotelcode)
    if kindercode == "A":
        prijs_kind = 0
    else:
        prijs_kind = volwassene_prijs / 2

    return  prijs_kind

hotelcode = input("Hotelcode (2letter 4 cijfers:" )

def druk_aantalsterren_af(aantal_sterren):
    for i in range(aantal_sterren):
        print("*", end="")
    print(end=" ")

while hotelcode != '/':
    aantal_volwassenen = int(input("Aantal volwassenen: "))
    aantal_kinderen = int(input("Aantal kinderen: "))

    aantal_sterren = int(input("Aantal sterren 1 - 5"))
    kindercode = input("Kindercode (A-Z)")
    while kindercode < 'A' or kindercode >'Z':
        aantal_personen = aantal_kinderen + aantal_volwassenen
        kindercode = input("Kindercode (A-Z)")
    print(hotelcode, end="")
    druk_aantalsterren_af(aantal_sterren)
    print(bereken_prijs_per_persoon(aantal_sterren,hotelcode), bereken_prijs_per_kind(aantal_kinderen, kindercode, aantal_sterren, hotelcode), bereken_prijs_per_persoon(aantal_sterren,hotelcode) + bereken_prijs_per_kind(aantal_kinderen, kindercode, aantal_sterren, hotelcode))
    hotelcode = input("Hotelcode (2letter 4 cijfers:")





