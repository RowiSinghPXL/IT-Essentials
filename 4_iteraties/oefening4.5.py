getal  = int(input("Geef een getal tussen 1 en 100."))

while(getal <= 1 or getal >= 100):
    if getal <= 1:
        print("Fout! Het getal moet groter zijn dan 1")
    else:
        print("Fout! Het getal moet kleiner zijn dan 100")
    getal = int(input("Geef een getal tussen 1 en 100."))

print("Ingegeven getal tussen 1 en 100 is", getal)