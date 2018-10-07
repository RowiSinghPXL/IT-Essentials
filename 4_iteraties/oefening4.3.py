som = 0
negatieve_getallen = 0
getal = int(input("Getal: "))

while getal != 0:
    som += getal
    if getal < 0:
        negatieve_getallen += 1
    getal = int(input("Getal: "))

print("De som van de getallen is", som)
print("Aantal negatieve getallen:", negatieve_getallen)
   