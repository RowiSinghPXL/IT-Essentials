geheel_getal = int(input("Geef een geheel getal in."))

for i in range(1, 21):
    print(i, "x", geheel_getal, "=", i * geheel_getal)

    # format  .format print({':2'} 'x' {':2'} = {:4}.format(i, "x", geheel_getal, "=", i * geheel_getal)) )