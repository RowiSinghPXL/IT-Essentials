leeftijd = int(input("geef leeftijd"))

if leeftijd < 12:
    lidgeld = 6
elif leeftijd < 18:
    lidgeld = 12.5
else:
    lidgeld = 25

print("Het lidgeld is €", lidgeld, "en de leeftijd is", leeftijd)