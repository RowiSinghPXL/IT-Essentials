lengte = float(input("Geef lengte in m"))
gewicht = float(input("Geef gewicht in kg"))

bmi = gewicht / lengte ** 2


if bmi < 18:
    print("Ondergewicht")
elif bmi < 25:
    print("Ok")
elif bmi < 30:
    print("Overgewicht")
elif bmi < 40:
    print("Obesitas")
else:
    print("Ziekelijk overgewicht")
