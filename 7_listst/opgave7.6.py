def cumulative_sum(nlijst):
    for i in range(1, len(nlijst)):
        nlijst[i] = (nlijst[i] + nlijst[i -1])



lijst = [4, 6, 12]
lijst = [1, 2, 3, 4, 5]
cumulative_sum(lijst)
print(lijst)

