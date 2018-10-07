brutoloon = float(input("Brutoloon"))

vakantiegeld = brutoloon * 0.05

if vakantiegeld >= 350:
    jaarlijkse_bijdrage = 350 * 1.08
else:
    jaarlijkse_bijdrage =  vakantiegeld * 1.08

print("brutoloon:", brutoloon, "euro", "vakantiegeld", vakantiegeld, "euro", "jaarlijkse bijdrage:", jaarlijkse_bijdrage, "euro" )

