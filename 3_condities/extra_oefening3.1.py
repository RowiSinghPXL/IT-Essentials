getal_a = int(input("Geef een waarde"))
getal_b = int(input("Geef een waarde"))
getal_c = int(input("Geef een waarde"))


som = getal_a + getal_b

if som < 20:
    som += getal_c
else:
    som = "te groot"

print("De uitkomst is", som)
