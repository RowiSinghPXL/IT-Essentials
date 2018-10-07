gewicht = float(input("gewicht"))

if gewicht > 20:
    print("Er moet een toeslag van €25 betaald worden voor bagage die te zwaar is")
elif gewicht < 20:
    print("Goede reis!")
else:
    print("Poeh!")
    