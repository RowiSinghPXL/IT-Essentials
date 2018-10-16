def bereken_hotel_kosten(aantal_nachten):
    hotel_kosten = 0
    for i in range(aantal_nachten):
        if i % 3 != 0:
            hotel_kosten += 140.50

    return hotel_kosten


def bereken_vliegtuig_kosten(stad):
    vliegtuig_kost = 0
    if stad == "Barcelona":
        vliegtuig_kost = 183
    elif stad == "Rome":
        vliegtuig_kost = 220
    elif stad == "Berlijn":
        vliegtuig_kost = 125
    elif stad == "Oslo":
        vliegtuig_kost = 450
    else:
        vliegtuig_kost = 0
    return vliegtuig_kost



def huurauto_kosten(aantal_dagen):
    prijs = aantal_dagen * 40

    if aantal_dagen > 7:
        prijs -= 50
    elif aantal_dagen > 3:
        prijs -= 20
    return prijs


def reis_kosten(stad, aantal_dagen, aantal_nachten):

    reiskosten = 0
    if bereken_vliegtuig_kosten(stad) == 0:

        return "Foutmelding"
    else:
        reiskosten = bereken_hotel_kosten(aantal_nachten) + bereken_vliegtuig_kosten(stad) + huurauto_kosten(aantal_dagen)
        return reiskosten




aantal_nachten = int(input("Geef het aantal nachten"))
stad = input("Geef een stad")
aantal_dagen = int(input("Aantal dagen huurauto"))

print(reis_kosten(stad,aantal_dagen, aantal_nachten))

