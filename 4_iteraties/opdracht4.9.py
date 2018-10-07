leeftijd = 0
totale_leeftijd = 0
for i in range(1, 29):
    leeftijd = int(input("Geef leeftijd van student " + str(i)))
    totale_leeftijd = leeftijd + totale_leeftijd

gemiddelde = totale_leeftijd / 28

print("De gemiddelde leeftijd is", gemiddelde)
print(i)

