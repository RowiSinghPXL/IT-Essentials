def bepaal_sterrenbeeld(lijst_sterrenbeelden, geboortedatum, lijst_maanden):
    sterrenbeeld = ""
    maand = geboortedatum[3:5]
    dag = geboortedatum[0:2]
    dag = int(dag)
    maand = int(maand)

    for i in range(12):
        if (dag >= 21 and i == maand):

            sterrenbeeld = lijst_sterrenbeelden[i - 1]
        elif (dag <= 20 and i == maand):
            sterrenbeeld = lijst_sterrenbeelden[i - 2]

    return sterrenbeeld

lijst_sterrenbeelden = ["waterman", "vissen", "ram", "stier", "tweelingen", "kreeft", "leeuw", "maagd", "weegschaal", "schorpioen", "boogschutter", "steenbok"]
lijst_maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]

geboortedatum = input("geboortedatum")

while geboortedatum != '/':
    naam = input("Naam")
    voornaam = input("Voornaam")
    sterrenbeeld = bepaal_sterrenbeeld(lijst_sterrenbeelden, geboortedatum, lijst_maanden)
    geboren = geboortedatum[0:5]
    print(voornaam[0] + "." + naam + " " + sterrenbeeld )
    geboortedatum = input("geboortedatum")





