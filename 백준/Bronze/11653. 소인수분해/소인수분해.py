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
def getDivNum(number):
    for i in range(2, number):
        if number % i == 0:
            return i
    return number

while N > 1:
    if not isPrime(N):
        divNum = getDivNum(N)
        print(divNum)
        N = N // divNum
    else:
        print(N)
        break
        
