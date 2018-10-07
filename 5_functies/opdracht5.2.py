def rij_sterren(tekens, aantal, hoogte):
    for i in range(hoogte):
        for i in range(aantal):
            print(tekens, end=" ")
        print()


tekens = input("Geef een teken")
aantal = int(input("Geef het aantal"))
hoogte = int(input("Geef de hoogte"))
rij_sterren(tekens, aantal, hoogte)
