nummer_lijst = []
som = 0
kleiner = 0
for i in range(0, 15):
    nummer = int(input("Geef getal" + str(i) + " een waarde."))
    nummer_lijst.append(nummer)

for i in range(0, 15):
    som += nummer_lijst[i]

gemiddelde = som / 15
gemiddelde = round(gemiddelde,1)

for i in range(0, 15):
    if nummer_lijst[i] < gemiddelde:
        kleiner += 1

procent = (kleiner / 15) * 100
print(gemiddelde)
print(kleiner)
print(procent, "%")

#constante maken voor die 15
#eerste en tweede lus kunnen samen 1 lus worden
#gemiddelde afronden of afkappen

