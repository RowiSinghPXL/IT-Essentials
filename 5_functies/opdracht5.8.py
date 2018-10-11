def berekening_verschuldigde_belasting(belastbaar_bedrag):
    belasting_1 = 0
    belasting_2 = 0
    belasting_3 = 0

    if belastbaar_bedrag > 55000:
        belasting_3 = (belastbaar_bedrag - 55000) * 0.6
        belastbaar_bedrag = 55000

    if belastbaar_bedrag > 25000 and belastbaar_bedrag <= 55000:
        belasting_2 = (belastbaar_bedrag - 25000) * 0.5
        belastbaar_bedrag = 25000

    if belastbaar_bedrag <= 25000:
        belasting_1 = belastbaar_bedrag * 0.384

#van klein naar groot beginnen if bedrag < 25000    else belasting = 25000 * 0.384 if   else

    #if:
    #else:
        #if:
        #else:

    totaal_tebetalen_belasting = belasting_1 + belasting_2 + belasting_3
    return totaal_tebetalen_belasting

belastbaar_bedrag = float(input("Belastbaar bedrag: "))
print("Belasting €", berekening_verschuldigde_belasting(belastbaar_bedrag))


if bedrag <= 25000:
    belasting = bedrag * 0.384
else:
     belasting = 25000 *0.384
        if
        else


