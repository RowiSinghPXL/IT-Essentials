getal = int(input("Bedrag in centen"))

muntstuk_twee_groot = getal // 200
getal = getal % 200

muntstuk_een_groot = getal // 100
getal = getal % 100

muntstuk_vijftig = getal // 50
getal = getal % 50


muntstuk_twintig = getal // 20
getal = getal % 20

muntstuk_tien = getal // 10
getal = getal % 10

muntstuk_vijf = getal // 5
getal = getal % 5

muntstuk_twee = getal // 2
getal = getal % 2

#muntstuk_een = getal // 1
#getal = getal % 1
muntstuk_een = getal

print("359 centen zijn", muntstuk_twee_groot ," X 2 euro", muntstuk_een_groot , " X 1 euro" , muntstuk_vijftig , " X 50 cent" , muntstuk_twintig , "  X 20 cent", muntstuk_tien, " X 10 cent" , muntstuk_vijf, " X 5 cent " , muntstuk_twee , " X 2 cent " , muntstuk_een , " X 1 cent.")



