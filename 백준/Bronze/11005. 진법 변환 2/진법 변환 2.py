numberCount = [ ]
N, B = map(int, input().split())
numberList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
answer = ''
while N:
    answer += str(numberList[N%B])
    N = N // B
print(answer[::-1])