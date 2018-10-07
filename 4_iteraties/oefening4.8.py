inschrijvingsnummer = int(input("Geef het inschrijvingsnummer in: "))
aantal_renners = 0
langer_dan_1_uur = 0
snelste_tijd = 0
snelste_renner = 0
while inschrijvingsnummer >= 0:
    tijd_in_seconden = int(input("Geef de tijd in seconden: "))
    aantal_renners += 1
    if snelste_tijd > tijd_in_seconden: # snelste kan in 1 if
        snelste_tijd = tijd_in_seconden
        snelste_renner = inschrijvingsnummer
    #else:
     #   if aantal_renners == 1:
        #    snelste_tijd = tijd_in_seconden
       #     snelste_renner = inschrijvingsnummer ####################""
    if tijd_in_seconden > 3600:
        langer_dan_1_uur += 1

    inschrijvingsnummer = int(input("Geef het inschrijvingsnummer in: "))


uur = snelste_tijd // 3600
min = (snelste_tijd % 3600) // 60
sec = (snelste_tijd % 3600) % 60
percentage_langer_dan_1_uur = langer_dan_1_uur / aantal_renners * 100
print("Senelste renner is de renner met inschrijvingsnummer:", snelste_renner)
print("De snelste renner deed hierover", uur, ".h", min, ".m", sec, ".s")
print("Het percentage van renners dat er langer dan 1 uur over doet:", percentage_langer_dan_1_uur, "%")

