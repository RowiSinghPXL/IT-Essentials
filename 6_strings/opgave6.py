woord = input("Woord: ")

lengte = len(woord)

if lengte % 2 != 0:
    middelste = lengte // 2
    print(woord[0:middelste] + woord[middelste].upper() + woord[middelste +1:])
else:
    middelste = lengte // 2
    print(woord[0:middelste -1] + woord[middelste - 1].upper() + woord[middelste].upper() + woord[middelste +1:])








#print( woord[0]+woord[1:lengte -1].upper() + woord[lengte -1])