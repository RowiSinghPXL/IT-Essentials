# burgerlijke_staat = int(input("Geef de burgerlijke staat (1. ongehuwd 2. gehuwd 3. weduwe): "))
#
# if burgerlijke_staat == 1:
#     lidgeld = 25
# elif burgerlijke_staat == 2:
#     lidgeld = 20
# else:
#     lidgeld = 15
#
# print("Het jaarlijks lidgeld bedraagt", lidgeld, "euro")


# burgerlijke_staat = int(input("Geef de burgerlijke staat (1. ongehuwd 2. gehuwd 3. weduwe): "))
# leeftijd = int(input("Geef uw leeftijd in: "))
#
# if leeftijd < 30 and burgerlijke_staat == 1:
#     lidgeld = 25
# else:
#     lidgeld = 15
#
# print("Het jaarlijks lidgeld bedraagt", lidgeld, "euro")


# burgerlijke_staat = int(input("Geef de burgerlijke staat (1. ongehuwd 2. gehuwd 3. weduwe): "))
# leeftijd = int(input("Geef uw leeftijd in: "))
#
# if leeftijd < 30 or burgerlijke_staat == 1:
#     lidgeld = 25
# else:
#     lidgeld = 15
#
# print("Het jaarlijks lidgeld bedraagt", lidgeld, "euro")


burgerlijke_staat = int(input("Geef de burgerlijke staat (1. ongehuwd 2. gehuwd 3. weduwe): "))
leeftijd = int(input("Geef uw leeftijd in: "))

if burgerlijke_staat == 1:
    lidgeld = 25
elif burgerlijke_staat == 2 and leeftijd < 30:
    lidgeld = 20
else:
    lidgeld = 15

print("Het jaarlijks lidgeld bedraagt", lidgeld, "euro")