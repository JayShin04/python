T = int(input())
coinList = (25, 10, 5, 1)

for i in range(T):
    restCoin = [ ]
    cents = int(input())
    for j in coinList:
        restCoin.append(cents // j)
        cents %= j
    for j in restCoin:
        print(j, end=' ')
        