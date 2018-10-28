#oefening kan korter
from random import randint
kleiner_dan_5000 = 0
groter_dan_5000 = 0
som = 0
som2 = 0


lijst = []

for i in range(0, 500):
    getal = randint(0, 10000) #bij random is bovengrens incl.
    lijst.append(getal)
    #if getal groter dan 5000 hier en tellen

for i in range(0, 500):
    print(lijst[i])
    if lijst[i] < 5000:
        kleiner_dan_5000 += 1
    else:
        groter_dan_5000 += 1

if kleiner_dan_5000 < 250:
    for i in range(0, 500):
        if lijst[i] > 5000:
            som += lijst[i]
    print("som kleiner 5000", som)

if groter_dan_5000 >= 250:
    for i in range(0, 500):
        if lijst[i] > 8000:
            som2 += lijst[i]
    print("som groter 5000", som2)

print(kleiner_dan_5000)
print(groter_dan_5000)

#ondergrens en som groter 5000 afdrukken ==> mjin oplossing drukt teveel af.

