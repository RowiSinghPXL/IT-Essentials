def rij_sterren(tekens, aantal):
    for i in range(aantal):
        print(tekens, end=" ")

tekens = input("Geef een teken")
aantal = int(input("Geef het aantal"))
rij_sterren(tekens, aantal)
