lengte = int(input("Geef de lengte: "))
breedte = int(input("Geef de breedte: "))

for i in range(breedte ):
    for i in range(lengte ):
        print("*", end = " ")
    print()

print()
print()
print()

for i in range(breedte):
    for j in range(lengte):
        if i == 0 or i == breedte - 1:
            print("*", end = " ")
        else:
            if j == 0 or j == lengte - 1:
                print("*", end = " ")
            else:
                print(" ", end=" ")
    print()
