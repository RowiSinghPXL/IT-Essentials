basis_prijs = 5
huidig_jaar = 2018
jaar = int(input("Van welk jaar is de film: "))
rating = int(input("Welke rating heeft de film (1 - 5): "))
prijs = basis_prijs

if huidig_jaar - jaar < 2:
    prijs += 1

if rating == 4 or rating == 5:
    prijs +=2
elif rating == 3 or rating == 2:
    prijs +=1

if prijs > 7:
    prijs = 7

print("De prijs voor de film is:", prijs)




