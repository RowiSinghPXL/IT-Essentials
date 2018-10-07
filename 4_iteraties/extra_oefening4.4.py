geslacht = int(input("1 = man, 2 = vrouw"))
slechte_conditie_man = 0
slechte_conditie_vrouw = 0

while geslacht == 1 or geslacht == 2:
    afstand_km = float(input("Afstand na 12 min lopen in km"))
    afstand_m = afstand_km * 1000

    conditie_getal = (afstand_m-504.9) / 44.73
    if geslacht == 1 and conditie_getal < 36:
        slechte_conditie_man += 1
    elif conditie_getal < 29:
        slechte_conditie_vrouw += 1
    geslacht = int(input("1 = man, 2 = vrouw"))

print("Aantal mannen met een slechte conditie", slechte_conditie_man)
print("Aantal vrouwen met een slechte conditie", slechte_conditie_vrouw)
