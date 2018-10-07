vertrekuur = int(input("Geef vertrekuur: "))
vertrekminuut = int(input("Geef vertrekmin: "))
duur = int(input("Geef duur: "))

minuten = vertrekuur * 60 + vertrekminuut + duur
aankomst_uur = minuten // 60 % 24
aakomst_min = minuten % 60

print("Het aankomstuur word", aankomst_uur, "de aankomstminuut wordt", aakomst_min)




