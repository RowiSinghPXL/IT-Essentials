#moet met een geneste for
groote_driehoek = int(input("Grote driehoek: "))

for i in range(0,groote_driehoek):
    for i in range(groote_driehoek):
        print("@", end="")
    print()
    groote_driehoek -= 1

