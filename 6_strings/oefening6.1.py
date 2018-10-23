#alle reguliere oefeningen maken aanbevolen extraoef 8 9 10
tekst = input("Tekst: ")
plaats = tekst.upper().find('T')

if plaats == -1:
    print("Er komt geen t in voor.")

if len(tekst) % 2 == 0:
    tekst = tekst.lower()
    print("t/T eerste komt voor op positie", plaats)
else:
    tekst = tekst.upper()
    print("t/T eerste komt voor op positie", plaats)

print(tekst)


