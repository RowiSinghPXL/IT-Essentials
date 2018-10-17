zin_1 = input("Zin1: ")
zin_2 = input("Zin2: ")

if len(zin_1) < len(zin_2):
   kleinste = len(zin_1)
else:
    kleinste = len(zin_2)


for i in range(kleinste):
    if zin_2[i] == zin_1[i]:
        print(zin_1[i], "op index", i)