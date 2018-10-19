tekst = input("Tekst: ")

nieuwe_tekst = ""
i =  len(tekst) - 1
for j in range(i, -1, -1):
    nieuwe_tekst += tekst[j]

print(nieuwe_tekst)