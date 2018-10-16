from random import randint
teller = 0
#geen return gebruiken en met boolean werken
def geef_feedback(getal, willekeurig_getal):
    if getal < willekeurig_getal:
        return "Groter"
    elif getal > willekeurig_getal:
        return  "Kleiner"
    else:
        return "Proficiat, getal geraden"


willekeurig_getal = randint(1, 10)
getal = int(input("Geef een getal in"))
print(geef_feedback(getal, willekeurig_getal))

while teller < 3 and geef_feedback(getal, willekeurig_getal) != "Proficiat, getal geraden": # feedback beter niet in het hoofdpprogramma

    getal = int(input("Geef een getal in"))
    print(geef_feedback(getal, willekeurig_getal))
    teller += 1




