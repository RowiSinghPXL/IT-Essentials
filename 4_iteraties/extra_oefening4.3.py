naam_manager = input("Naam van manager: ")

while naam_manager != "xx" and naam_manager != "XX":

    examen_uitslag1 = float(input("Uitslag examen"))
    examen_uitslag2 = float(input("Uitslag examen"))
    examen_uitslag3 = float(input("Uitslag examen"))

    gemiddelde = (examen_uitslag1 + examen_uitslag2 + examen_uitslag3) / 3

    if gemiddelde < 70:
        uitslag = "De manager heeft gefaald"
    else:
        uitslag = "De manager is een succes"
    print(naam_manager, "Test1:", examen_uitslag1, "Test2:", examen_uitslag2, "Test3:", examen_uitslag3, "Gemiddelde:", gemiddelde, "Resultaat: ", uitslag)
    naam_manager = input("Naam van manager: ")
