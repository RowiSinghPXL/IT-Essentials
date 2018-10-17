def maken_van_nieuwe_string(zin):
    i = 0
    nieuwe_zin = ""
    for i in range(len(zin)):
        if ord(zin[i]) < 97 or ord(zin[i]) > 122:
            nieuwe_zin += " "
        else:
            nieuwe_zin += zin[i]

    return nieuwe_zin


zin = input("zin: ")

print(maken_van_nieuwe_string((zin)))






