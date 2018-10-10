def is_even(getal):
    if getal % 2 == 0:
        return True
    else: # zie functie vorige opdracht
        return False

def is_oneven():
    if is_even(getal):
        return False
    else:
        return True
    #return not is_even(getal) kan korter

getal = int(input("Geef een getal in: "))
print(is_oneven())
