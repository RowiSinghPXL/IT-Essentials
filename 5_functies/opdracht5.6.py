def get_tienden(getal):
    tiende = getal - (int(getal))
    tiende = tiende * 10
    tiende = int(tiende)
    return tiende

    #module 10 doen gaat korter     return int(getal % 1 * 10) |||| int(getal * 10) % 10


getal = float(input("Geef een kommagetal"))

print(get_tienden(getal))