def schrikkeljaar(jaartal):
    if (jaartal % 4 == 0 and jaartal % 100 != 0) or jaartal % 400 == 0: # kan zonder if en else als je gwn return gebruikt
        return True
    elif jaartal % 400 == 0: # deze elif mag weg

        return True
    else:

        return False

jaartal = int(input("Geef een jaartal in: "))
print(schrikkeljaar(jaartal))

