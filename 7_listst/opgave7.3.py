#append
#list zijn muteble woord = woord.upper()
#fruit=fruit.remove() ==> fout

getallen_lijst = []
getal = int(input("Geef een getal in:"))

while getal != 0:
    for i in range(len(getallen_lijst)):
        if getallen_lijst[i] == getal:
            print("Dit getal bevindt zich al in de lijst op plaats", i)
            getallen_lijst.remove(getal)
            i -= 1
    getallen_lijst.append(getal)
    getal = int(input("Geef een getal in:"))

print(getallen_lijst)