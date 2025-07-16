basket = [ 0 ]
N, M = map(int, input().split())
for i in range(1, N+1):
    basket.append(i)

for m in range(1, M+1):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]


for i in range(1, N+1):
    print(basket[i], end=' ')