def omzetten_in_min(in_uur, in_min, uit_uur, uit_min):
    minuten_aankomst = in_uur * 60 + in_min
    minuten_vertrek = uit_uur * 60 + uit_min
    duur = minuten_vertrek - minuten_aankomst
    return duur

in_uur = int(input("In uur"))
in_min = int(input("In min"))

uit_uur = int(input("uit_uur"))
uit_min = int(input("uit_uur"))




gemiddelde_aanwezigheidsduur = 0
meer_dan_een_uur = 0
totaal = 0
teller = 0

while in_uur != 0:
    if omzetten_in_min(in_uur, in_min, uit_uur, uit_min) > 60:
        meer_dan_een_uur += 1
    teller += 1
    totaal += omzetten_in_min(in_uur, in_min, uit_uur, uit_min)
    in_uur = int(input("In uur"))

gemiddelde_aanwezigheidsduur = totaal / teller

print("Aantal bezoekers langer dan 1 uur", meer_dan_een_uur)
print("Gemiddelde duur van bezoekers", gemiddelde_aanwezigheidsduur)




