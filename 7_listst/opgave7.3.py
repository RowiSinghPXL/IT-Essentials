#append
#list zijn muteble woord = woord.upper()
#fruit=fruit.remove() ==> fout

getallen_lijst = []
getal = int(input("Geef een getal in:"))

while getal != 0:

    if getal in getallen_lijst: #if getal in lijst
        print("Dit getal bevindt zich al in de lijst op plaats")
        print("het getal komt al voor op index", getallen_lijst.index(getal))

    else:

        getallen_lijst.append(getal)
    getal = int(input("Geef een getal in:"))

print(getallen_lijst)