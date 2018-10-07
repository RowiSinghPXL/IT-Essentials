resultaat1 = int(input("Resultaat eerste test op 20: "))
resultaat2 = int(input("Resultaat tweede test op 20: "))
resultaat3 = int(input("Resultaat derde test op 20: "))

totale_resultaat = (resultaat1 + resultaat2 + resultaat3) / 3 * 100

if totale_resultaat < 60:
    uitslag = "onvoldoende"
elif totale_resultaat < 70:
    uitslag = "voldoende"
elif totale_resultaat < 80:
    uitslag = "onderscheiding"
elif totale_resultaat < 90:
    uitslag = "grote onderscheiding"
else:
    uitslag = "grootste onderscheiding"

print("De student haalde", totale_resultaat,"% en heeft hiermee een", uitslag, "behaald")

