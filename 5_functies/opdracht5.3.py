def printx():
    print("x", end=" ")

def meerdere_x(aantal):
    for i in range(aantal):
        printx()

aantal = int(input("Hoevaak wil je dat x wordt afgedrukt"))
meerdere_x(aantal)
