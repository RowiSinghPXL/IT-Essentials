teller = 0
keuze = int(input("Geef een keuze: "))
lijst_kanidaten = [0, 0, 0, 0] #OF [0] * 4
lijst_kanidaat_namen = ["An Janssen", "Bart Vriends", "Andries Michels", "Inge Kaas"]

while keuze != 0:
    teller += 1
    if keuze == 1:
        lijst_kanidaten[0] += 1
    elif keuze == 2:
        lijst_kanidaten[1] += 1
    elif keuze == 3:
        lijst_kanidaten[2] += 1
    elif keuze == 4:
        lijst_kanidaten[3] += 1
    keuze = int(input("Geef een keuze: "))


for i in range(4):
    print("kanidaat " + str(i) + lijst_kanidaat_namen[i] + " heeft " + str(lijst_kanidaten[i]) + " stemmen." + "procentueel aandeel " + str((lijst_kanidaten[i] / teller) * 100))

