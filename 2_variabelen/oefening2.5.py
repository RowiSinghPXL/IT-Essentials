graden_in_fahrenheit = float(input("Geef het aantal graden in Fahrenheit"))


graden_in_celcius = (graden_in_fahrenheit -32) / 1.8


afgerond_op_een_decimaal = (graden_in_celcius * 100)
afgerond_op_een_decimaal = int(afgerond_op_een_decimaal)
afgerond_op_een_decimaal = afgerond_op_een_decimaal + 5
afgerond_op_een_decimaal = afgerond_op_een_decimaal / 10
afgerond_op_een_decimaal = int(afgerond_op_een_decimaal)
afgerond_op_een_decimaal = afgerond_op_een_decimaal / 10

print(graden_in_fahrenheit , "F is gelijk aan " , afgerond_op_een_decimaal, "C")