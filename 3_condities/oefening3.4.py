getal1 = float(input("Geef een getal in: "))
getal2 = float(input("Geef een getal in: "))

if getal1 < getal2:
    kleinste_getal = getal1
    grootste_getal = getal2
else:
    kleinste_getal = getal2
    grootste_getal = getal1

if kleinste_getal == 0:
    antwoord = "Je kan niet delen door nul"
else:
    antwoord = grootste_getal / kleinste_getal

print("Het kleinste getal is", kleinste_getal, "Het kwadraat van het kleinste getal is", kleinste_getal**2,"Het grootste getal gedeeld door het kleinste getal is", antwoord)
    