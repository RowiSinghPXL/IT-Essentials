teller = 0
tekst = input("Geef een tekst: ")
letters = "a, b, c, d,e"
alle_letter = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,,Y,Z"
#lijst maken aantal keer voor intialiseren met 0 ==> frequentietabel lijst = [0] * 26

#met functie ord van letter ==> cijfers

#ascii waarden met je eigen waarden gelijk maken ascci - 97

lijst_alle_letters = alle_letter.split(",")
letters_voorkomen = []

tekst = tekst.upper()

for i in range(0, len(tekst)):
    for j in range(0, len(lijst_alle_letters)):
        if lijst_alle_letters[j] in tekst:
            teller = tekst.count(lijst_alle_letters[j])
            letters_voorkomen.append(teller)
        else:
            teller += 0
            letters_voorkomen.append(teller)

for i in range(0, len(tekst)):
    if letters_voorkomen[i] > 0:
        print(lijst_alle_letters[i], "komt", letters_voorkomen[i], "keer voor")

#kan ook zonder frequentie tabel
#met count functie  tekst.lower().count(chr(letter)))




