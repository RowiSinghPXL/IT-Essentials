numberlist = [314, 315, 642, 246, 999, 129]
#!eerste listitem in de max of min steken
grootste_waarde = numberlist[0] #eerste lijstnumber in var steken
som = 0
kleinstewaarde = numberlist[0]

for i in range(1, len(numberlist)): #minder testen drm start je vanaf 1
    if grootste_waarde < numberlist[i]:
        grootste_waarde = numberlist[i]
    if kleinstewaarde > numberlist[i]:
        kleinstewaarde = numberlist[i]
    som += numberlist[i]

print("grootste waarde:", grootste_waarde)
print("kleinste waarde:", kleinstewaarde)
print("som:", som)
#1) alle elementen in de lijst
#maximum = max(getallenlijst)
