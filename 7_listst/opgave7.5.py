def druk_kopies_af(list, element):
    aantal_keer = list.count(element)
    return aantal_keer

lijst = [1, 2, 3, 4, 4, 5, 6, 7, 7]
element = int(input("Welk getal wil je zoeken"))
print(element, "komt", druk_kopies_af(lijst,element) ,"keer voor")

#indexen
#lege lijst toevoegen

