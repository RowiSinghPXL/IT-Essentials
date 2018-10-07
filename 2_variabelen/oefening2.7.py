lengte = input("Lengte in meter: ")
lengte = float(lengte)

breedte = input("Breedte in meter: ")
breedte = float(breedte)

plaatsings_kosten = input("Plaatsing kosten")
plaatsings_kosten =  float(plaatsings_kosten)

prijs_per_vierkante_meter = input("Prijs per vierkante meter")
prijs_per_vierkante_meter = float(prijs_per_vierkante_meter)

vierkante_meter = lengte * breedte

totale_prijs = plaatsings_kosten * vierkante_meter + prijs_per_vierkante_meter * vierkante_meter

print("De totale prijs bedraagt: ", totale_prijs, "euro")
