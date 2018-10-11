def controlee(lidnummer):
    tweede_cijfer = int(lidnummer / 100000)
    tweede_cijfer = tweede_cijfer % 10

    vierde_cijfer = int(lidnummer / 1000)
    vierde_cijfer = vierde_cijfer % 10

    twee_laatste_cijfers = int(lidnummer % 100)
    twee_laatste_cijfers = str(twee_laatste_cijfers)

    tweede_en_vierde_samen = str(tweede_cijfer) + str(vierde_cijfer)

    if tweede_en_vierde_samen == twee_laatste_cijfers:
        return "gratis"
    else:
        return "inkom betalen"



lidnummer = float(input("Geef de lidnummer: "))

print(controlee(lidnummer))