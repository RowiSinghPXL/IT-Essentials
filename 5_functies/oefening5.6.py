from random import randint

for i in range(1,6):
    print("reeks", i)
    for i in range(1,6):
        getal_1 = randint(0,20)
        getal_2 = randint(0,20)
        while getal_2 > getal_1:
            getal_2 = randint(0,20)
        print(i,")", getal_1, "-", getal_2, "=")
    print()





