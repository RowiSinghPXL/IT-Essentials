personeelsnummer = int(input("Personeelsnummer: "))
aantal_man_met_voorwaarde = 0
jonge_vrouw = 0

while personeelsnummer != 0:
    geslacht = int(input("0= vrouw; 1= man"))
    while geslacht != 1 and geslacht != 0:
        geslacht = int(input("0= vrouw; 1= man"))
    leeftijd = int(input("Leeftijd:"))
    brutoloon = int(input("Brutoloon: "))

    if geslacht == 1: # geneste if maken if geslacht == 0 if brutoloon > 1800 or leeftijd > 34 vergroot de leesbaarheid
        if leeftijd > 34 or brutoloon > 1800:
            aantal_man_met_voorwaarde += 1
    elif  leeftijd < 25: # geslacht niet opnieuw testen zie lijn 7
        jonge_vrouw += 1
    personeelsnummer = int(input("Personeelsnummer: "))

print("Aantal mannen die ouder zijn dan 34 of een loon van meer dan 1800 euro:", aantal_man_met_voorwaarde)
print("Aantal vrouwen dat jonger is dan 25", jonge_vrouw)

