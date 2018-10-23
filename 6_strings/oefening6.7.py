from random import randint

def encrypteren(tekst, getal):
    encryptie = ""

    for i in range(len(tekst)):
        hulp = ord(tekst[i]) + getal
        hulpstring = chr(hulp)
        encryptie += hulpstring
    return encryptie

ingevoerde_tekst = input("Geef een tekst")
gegenereerde_getal = randint(2, 25)

while gegenereerde_getal % 2 == 0:
    gegenereerde_getal = randint(2, 24)

print(encrypteren(ingevoerde_tekst, gegenereerde_getal))

