def get_tienden(getal):
    tiende = getal - (int(getal))
    tiende = tiende * 10
    return  int(tiende)


getal = float(input("Geef een kommagetal"))

print(get_tienden(getal))