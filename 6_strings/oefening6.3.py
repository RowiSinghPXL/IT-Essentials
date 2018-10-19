aantal_karakters_ingeven = int(input("Aantal karakters ingeven: "))
som = 0
for i in range(aantal_karakters_ingeven):
    karakter = input("Geef een karakter in: ")
    if karakter >= 'A' and karakter <= 'Z':
        print("karakter is een hoofdletter")
    elif karakter >= 'a' and karakter <= 'z':
        print("karakter is een kleine letter")
    elif karakter >= '0' and karakter <= '9':
        karakter = int(karakter)
        som += karakter
    else:
        print("Onbekend")
print("De som bedraagt", som)



