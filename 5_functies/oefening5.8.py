def bereken_kostprijs(aantal_vierkante_meter):
    prijs = (aantal_vierkante_meter / 160) * 12.5
    return prijs

def bereken_nodige_personeel(aantal_vierkante_meter):
    tijd = aantal_vierkante_meter / 160

    if tijd < 8:
        aantal_personen = 1
    else:
        aantal_personen = tijd / 8
        if tijd % 8 > 0:
            aantal_personen = aantal_personen +1
    return int(aantal_personen)



persoon_rest = 0


aantal_schoon_te_maken_vierkante_meter = int(input("Aantal schoon te maken vierkante meter: "))

while aantal_schoon_te_maken_vierkante_meter != 0:

    if aantal_schoon_te_maken_vierkante_meter / 160 > 8:
        persoon_rest = int((aantal_schoon_te_maken_vierkante_meter / 160) % 8)


    print("De totale prijs is:", bereken_kostprijs(aantal_schoon_te_maken_vierkante_meter))
    print("Aantal mankracht nodig:", bereken_nodige_personeel(aantal_schoon_te_maken_vierkante_meter))
    print(bereken_nodige_personeel(aantal_schoon_te_maken_vierkante_meter) - 1, "werk(t-en) 8 uur", "1 persoon werkt", persoon_rest)

    aantal_schoon_te_maken_vierkante_meter = int(input("Aantal schoon te maken vierkante meter: "))
