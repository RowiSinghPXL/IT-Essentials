def get_number_of_participants(heartrates):
    participants = len(heartrates[0])
    return participants

def get_number_of_tests(heartrates):
    tests = len(heartrates)
    return tests

def highest_heart_rate(heartrates):

    grootste = 0
    for i in range(get_number_of_tests(heartrates)):
        for j in range(get_number_of_participants(heartrates)):
            if heartrates[i][j] > grootste:
                grootste = heartrates[i][j]
    return grootste

def lowest_heart_rate(heartrates):
    kleinste = highest_heart_rate(heartrates)
    for i in range(get_number_of_tests(heartrates)):
        for j in range(get_number_of_participants(heartrates)):
            if heartrates[i][j] < kleinste:
                kleinste = heartrates[i][j]
    return kleinste

def average_heart_rate(heartrates):
    #averge = []
    total_sum = 0
    total = get_number_of_participants(heartrates) * get_number_of_tests(heartrates)

    for i in range(get_number_of_tests(heartrates)):
        for j in range(get_number_of_participants(heartrates)):
            total_sum += heartrates[i][j]

    average = total_sum / total
    #averges.append(roudn(sum/ number_of_participants, 2)
    #return avergas list teruggeven

    return average

def heart_rate_difference(heartrates):
    results = []
    numer_of_participants = get_number_of_participants(heartrates)
    numer_of_test = get_number_of_tests(heartrates)
    for participant in range(numer_of_participants):
        higest = heartrates[0][participant]
        lowest = heartrates[0][participant]
        for test in range(1, get_number_of_tests):
            if heartrates[test] [participant] > higest:
                higest = heartrates[test][participant]
            if heartrates[test][participant] < lowest:
                lowest = heartrates[test][participant]
        results.append(higest - lowest)
        return results

heartrates = [[72, 75, 71, 73, 72, 76], [91, 90, 94, 93, 88, 91], [130, 135, 139, 142, 129, 138], [130, 135, 139, 142, 129, 138]]
difference = []
difference = heart_rate_difference(heartrates, difference)

print("Participants:", get_number_of_participants(heartrates))
print("Tests:", get_number_of_tests(heartrates))
print("Highest:", highest_heart_rate(heartrates))
print("Lowest:", lowest_heart_rate(heartrates))
print("Average:", average_heart_rate(heartrates))
print(difference)












#print(" ", end="")
#for i in range(6):
 #   print("Deelnemer", i, "\t", end="")

#for rij in range(4):
 #   print()
  #  for kol in range(6):
   #     print(heartrates[rij] [kol], end="\t")

