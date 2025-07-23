M = int(input())
N = int(input())

def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
numberList = []
for i in range(M, N+1):
    if isPrime(i):
        numberList.append(i)

if len(numberList) != 0:
    print(sum(numberList))
    print(min(numberList))
else:
    print(-1)