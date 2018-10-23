def bereken_verschil(lengte_tekst):
    verschil = 0
    verschil = 4 - lengte_tekst
    return verschil

tekst_1 = input("Geef tekst 1: ")
tekst_2 = input("Geef tekst 2: ")
lengte_tekst_1 = len(tekst_1)
lengte_tekst_2 = len(tekst_2)
laatste_4_tekst_2 =""

if lengte_tekst_1 >= 4:
    eerste_4_tekst_1 = tekst_1[0:4]
else:
    vershil = bereken_verschil(lengte_tekst_1)
    eerste_4_tekst_1 = tekst_1[0:lengte_tekst_1]
    for i in range(vershil):
        eerste_4_tekst_1 += "*"

if lengte_tekst_2 >= 4:
    laatste_begin = lengte_tekst_2 - 4
    laatste_4_tekst_2 = tekst_2[laatste_begin:]
else:
    vershil = bereken_verschil(lengte_tekst_2)
    for i in range(vershil):
        laatste_4_tekst_2 += "+"
    laatste_4_tekst_2 += tekst_2

print(eerste_4_tekst_1, end="")
print(laatste_4_tekst_2)


