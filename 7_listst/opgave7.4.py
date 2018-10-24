getallen_lijst = []
kleiner_dan_gemiddelde = 0
som = 0
for i in range(10):
    getal = int(input("Geef een getal: "))
    getallen_lijst.append(getal)
    som += getallen_lijst[i]

gemiddelde = som / len(getallen_lijst)

for i in range(10):
    if getallen_lijst[i] < gemiddelde:
        kleiner_dan_gemiddelde += 1

print("gemiddelde:", gemiddelde)
print("Aantal getallen kleiner dan gemiddelde:", kleiner_dan_gemiddelde)

