spreuk = "abracadabra"

nieuwe_spreuk = spreuk.replace('a','o')

teller = 0
for i in range(len(nieuwe_spreuk)):
    if nieuwe_spreuk[i]=='o':
        teller += 1
print("De o komt", teller, "keer voor")
print(nieuwe_spreuk)

#methode count : tele

print(spreuk.count("o"))