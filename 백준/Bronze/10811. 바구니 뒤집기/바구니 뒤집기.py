import sys
input = sys.stdin.readline
N, M = map(int, input().split())
basket = []
for i in range(1, N+1):
    basket.append(i)
for m in range(M):
    i, j = map(int, input().split())
    cha = j - i
    for k in range(cha):
        if i - 1 + k > j - 1 - k:
            continue
        basket[(i-1)+k], basket[(j-1)-k] = basket[(j-1)-k], basket[(i-1)+k]



for i in basket:
    print(i, end=' ')