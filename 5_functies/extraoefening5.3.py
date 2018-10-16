def controle_perfect_getal(getal):
    optelling = 0

    for i in range(getal -1, 0, -1):
        if getal % i == 0:
            optelling += i

    if optelling == getal:
        print("perfect getal")
    else:
        print("Geen perfect getal")


getal = int(input("Geef een getal in"))
controle_perfect_getal(getal)
