def berekenen_kinderbijslag(aantal_kinderen, leeftijd, code, hoeveelste_kind):

    if code == "H":
        bijslag = 300
    else:
        bijslag = 75

    if hoeveelste_kind > 0:
        bijslag += 70

    if leeftijd > 6:
        bijslag +=25
    elif leeftijd > 12:
        bijslag += 50

    return  bijslag


i = 1
totaal = 0
aantal_kinderen = int(input("Aantal kinderen: "))
for i in range(aantal_kinderen ):
    leeftijd = int(input("leeftijd"))
    code = input("Code")
    hoeveelste_kind = i
    totaal += berekenen_kinderbijslag(aantal_kinderen, leeftijd, code, hoeveelste_kind)

print("kindergeld:", totaal)