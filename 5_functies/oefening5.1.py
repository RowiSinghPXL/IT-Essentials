def euro_naar_dollar(waarde_dollar, bedrag_euro):
   bedrag_dollar = bedrag_euro * waarde_dollar
   #print("€",bedrag_euro, "is gelijk aan $", bedrag_dollar)
   return bedrag_dollar


bedrag_euro = float(input("Geef het aantal euro's"))
bedrag_dollar = 0

while bedrag_euro != 0:
    waarde_dollar = float(input("Hoeveel dollar is 1 euro"))
    print("€", bedrag_euro, "is gelijk aan", euro_naar_dollar(waarde_dollar,bedrag_euro))

    bedrag_euro = float(input("Geef het aantal euro's"))


