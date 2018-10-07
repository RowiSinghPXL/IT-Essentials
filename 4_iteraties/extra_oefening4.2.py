naam = input("Naam: ")

while naam != "xx" and naam != "XX":
    behaald_percentage = float(input("Behaald percentage: "))
    while behaald_percentage < 0 or behaald_percentage > 100:
        if behaald_percentage < 0:
            print("Het getal moet minstens 0 zijn")
        else:
            print("Het getal mag max. 100 zijn")
        behaald_percentage = float(input("Behaald percentage: "))

    if behaald_percentage < 60:
        uitslag = "onvoldoende"
    elif behaald_percentage < 70:
        uitslag = "voldoende"
    elif behaald_percentage < 80:
        uitslag = "onderscheiding"
    elif behaald_percentage < 85:
        uitslag = "grote onderscheiding"
    else:
        uitslag = "grootste onderscheiding"

    print("uitslag", naam, uitslag)
    naam = input("Naam: ")






