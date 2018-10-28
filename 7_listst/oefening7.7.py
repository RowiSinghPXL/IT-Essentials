def bereken_leeftijd(geboortedaum):
    leeftijd = 0
    jaar = int(geboortedatum[6:8])
    leeftijd = 2018 - jaar

    return leeftijd

def bereken_punten():
    if juist:
        punten += 2
    elif != 'E':
        punten -= 1
aantal_studenten = 0
deenemersnummer = int(input("Deelnemersnummer: "))
lijst_antwoorden = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B']
while deenemersnummer !=0:
    geboortedatum = input("Geboortedatum: ")
    lijst_antwoorden_student = []

    lijst_deelnemer_nr = []
    leeftijd_lijst = []
    tijd_lijst = []
    punten_lijst = []

    for i in range(10):
        aantal_studenten += 1
        lijst_deelnemer_nr.append(deenemersnummer)
        antwoord = input("Geef je antwoordt op vraag" + str(i) +": ")
        lijst_antwoorden_student.append(antwoord)
    tijd_in_sec = int(input(" de tijd in sec waarin de vragen werden beantwoord: "))
    leeftijd = bereken_leeftijd(geboortedatum)
    deenemersnummer = int(input("Deelnemersnummer: "))

for i in range(aantal_studenten):
    teller = i
    deenemersnummer = deenemersnummer[i]
    leeftijd = leeftijd_lijst[i]
    tijd = tijd_lijst[i]
    punten = punten[i]
    lijst_resultaten = [[teller] [deenemersnummer] [leeftijd] [tijd] [punten]] * aantal_studenten


