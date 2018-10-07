percentage_gewicht_maan = float(input("Percentage gewicht maan: ")) / 100
percentage_gewicht_jupiter = float(input("Percentage gewicht jupiter: ")) / 100
percentage_gewicht_mars = float(input("Percentage gewicht mars: ")) / 100

for i in range(50, 121, 5):
    print("Aarde:", i)
    print("Maan:", round(i * percentage_gewicht_maan,2))
    print("Jupiter:", round(i * percentage_gewicht_jupiter,2))
    print("Mars::", round(i * percentage_gewicht_mars,2))
    print()



