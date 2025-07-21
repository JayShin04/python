def isPrime(temp):
    if temp == 2:
        return True
    elif temp == 1:
        return False
    elif temp <= 0:
        return False
    for i in range(2, temp):
        if temp % i == 0:
            return False
    return True

N = int(input())
number = list(map(int, input().split()))
for i in number:
    if isPrime(i):
        number[number.index(i)] = 1
    else:
        number[number.index(i)] = 0

print(sum(number))

