HUIDIG_JAAR = 2018

bedrag = 100
leeftijd = int(input("leeftijd"))
aansluitingsjaar = int(input("aansluitingsjaar"))

if leeftijd < 21 or leeftijd > 60:
    bedrag -= 14.5

jarenlid = HUIDIG_JAAR - aansluitingsjaar #in 1 var
bedrag -= jarenlid * 2.5 #in 1 var

if bedrag < 62.5:
    bedrag = 62.5

print("Het te betalen bedrag is", bedrag, "euro")


