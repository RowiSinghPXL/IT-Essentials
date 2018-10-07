getal_a = int(input("Geef getal a een waarde"))
getal_b = int(input("Geef getal b een waarde"))
code = int(input("Geef een bewerkingscode in"))

if code == 1:
    uitkomst = getal_a + getal_b
    print(getal_a,"+",getal_b,"=", uitkomst)
elif code == 2:
    uitkomst = getal_a - getal_b
    print(getal_a, "-", getal_b, "=", uitkomst)
elif code == 3:
    uitkomst = getal_a * getal_b
    print(getal_a, "*", getal_b, "=", uitkomst)
elif code == 4:
    uitkomst = getal_a ** 2
    print("Het kwadraat van", getal_a, "=", uitkomst)
elif code == 5:
    uitkomst = getal_b ** 2
    print("Het kwadraat van", getal_b, "=", uitkomst)
else:
    uitkomst = "Foutieve code"


