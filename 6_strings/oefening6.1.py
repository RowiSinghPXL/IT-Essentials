#alle reguliere oefeningen maken aanbevolen extraoef 8 9 10
tekst = input("Tekst: ")
plaats = tekst.upper().find('T')
print("t/T eerste komt voor op positie", plaats)
if plaats == -1:
    print("Er komt geen t in voor.")

if len(tekst) % 2 == 0:
    tekst = tekst.lower()
else:
    tekst = tekst.upper()

print(tekst)


