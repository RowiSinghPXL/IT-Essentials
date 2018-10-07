hoogste_temperatuur = -99
totale_temperatuur = 0

for i in range(1, 13):
    temperatuur = float(input("Geef de gemeten temperatuur van 12u 's middags"))
    if (temperatuur > hoogste_temperatuur):
        hoogste_temperatuur = temperatuur
    totale_temperatuur += temperatuur

print()
print("De hoogste tempartuur is:", hoogste_temperatuur)
print("De gemiddelde temperatuur is:", totale_temperatuur/i ) #i+1

