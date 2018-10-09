def euro_naar_dollar(waarde_dollar, bedrag_euro):
   bedrag_dollar = bedrag_euro * waarde_dollar
   print("€",bedrag_euro, "is gelijk aan $", bedrag_dollar)

waarde_dollar = float(input("Hoeveel dollar is 1 euro"))
bedrag_euro = float(input("Geef het aantal euro's"))
bedrag_dollar = 0

while bedrag_euro != 0:

    euro_naar_dollar(waarde_dollar, bedrag_euro)
    bedrag_euro = float(input("Geef het aantal euro's"))

