positieve_getallen = []
negatieve_getallen = []
kleinste_getal = 0

for i in range(0, 10):
    getal = int(input("Getal"))
    if getal >= 0:
        positieve_getallen.append(getal)
    else:
        negatieve_getallen.append(getal)


for i in range(0, len(negatieve_getallen)):
    if negatieve_getallen[i] < kleinste_getal:
        kleinste_getal = negatieve_getallen[i]

print(positieve_getallen)
print(negatieve_getallen)
print(kleinste_getal)

