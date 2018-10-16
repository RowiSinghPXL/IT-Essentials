def benadering_pi(termen):
    teller = 1
    temp_uit = 0
    breuk_a = 0
    noemer = 1
    for i in range(termen - 1):
        if i % 2 == 0:
            breuk_a = 1/noemer
            noemer += 2
        else:
            breuk_b = 1/noemer
            temp_uit = breuk_a - breuk_b
            noemer += 2
        temp_uit += temp_uit
    tot_uit = temp_uit * 4
    return  tot_uit

hoeveel_termen = int(input("Aantal termen"))
print(benadering_pi(hoeveel_termen))