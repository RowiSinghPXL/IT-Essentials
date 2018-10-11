def schrikkeljaar(jaartal):
    if jaartal % 4 == 0 and jaartal % 100 != 0:
        return True
    elif jaartal % 400 == 0:

        return True
    else:

        return False

jaartal = int(input("Geef een jaartal in: "))
print(schrikkeljaar(jaartal))

