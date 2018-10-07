getal = int(input("Bedrag in centen"))

muntstukTweeG = getal // 200
getal = getal % 200

muntstukEenG = getal // 100
getal = getal % 100

muntstukVijftig = getal // 50
getal = getal % 50


muntstukTwintig = getal // 20
getal = getal % 20

muntstukTien = getal // 10
getal = getal % 10

muntstukVijf = getal // 5
getal = getal % 5

muntstukTwee = getal // 2
getal = getal % 2

muntstukEen = getal // 1
getal = getal % 1

print("359 centen zijn", muntstukTweeG ," X 2 euro", muntstukEenG , " X 1 euro" , muntstukVijftig , " X 50 cent" , muntstukTwintig , "  X 20 cent", muntstukTien, " X 10 cent" , muntstukVijf, " X 5 cent " , muntstukTwee , " X 2 cent " , muntstukEen , " X 1 cent.")