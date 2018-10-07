aantal_sterren = int(input("aantal sterren:"))
code = input("O - H - V - A")
aantal_overnachtingen = int(input("aantal overnachtingen"))
seizoen = input("H - L - T")

prijs = 0

if aantal_sterren >= 4:
    prijs += 55         #formule niet in de if else beter na de if bereken factor van maken
elif aantal_sterren >= 2:
    prijs += 40
else:
    prijs += 30


if code == "O":
    prijs *= 1.2
    if seizoen == "L":
        prijs *= 0.9 #zie regel 20
elif code == "H":
    prijs *= 1.5
    if seizoen == "L":
        prijs *= 0.9 #zie regel 20
elif code == "V":
    prijs *= 1.6
else:
    prijs = (prijs * 1.6) + (80 * aantal_overnachtingen) + (prijs * aantal_overnachtingen)


if seizoen == "L" and (code =="H" or code=="O"):
    prijs *= 0.9
print ("De prijs is: €", prijs)


