def schrikkeljaar(jaartal):
    if jaartal % 4 == 0 and jaartal % 100 != 0:
        return True
    elif jaartal % 400 == 0:
        uitkomst = bool
        return True
    else:
        uitkomst = bool
        return False

jaartal = int(input("Geef een jaartal in: "))
print(schrikkeljaar(jaartal))

