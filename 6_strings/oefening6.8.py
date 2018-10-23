groote = int(input("Groote van driehoek"))
beginletter = input("Beginletter")

letter = beginletter
hulp = ord(letter) -1
letter = chr(hulp)

for i in range(groote +1):
    for j in range(i):
        hulp = ord(letter) +1
        letter = chr(hulp)
        if letter == '[':
            letter = 'A'
        print(letter, end=" ")
    print()