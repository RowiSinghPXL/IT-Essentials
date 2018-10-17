tekst = input("Geef een zin")
waardes ="aeiou"

for letter in tekst:
    if letter in waardes:
        print(letter, end=" ")
print()

teller = 1
for i in range(len(tekst)):
    letter = tekst[i]
    if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
       print(teller, end=" ")
    teller +=1


#kleiner
#beter

def is_klinker(teken):
    return teken in "aeiou"

tekst = "hallo"

for i in range(0, len(tekst)):
    if is_klinker(tekst[i]):
        print(i)

