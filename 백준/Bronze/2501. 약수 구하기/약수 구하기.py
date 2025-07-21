N, K = map(int, input().split())
divisor = [ ]
# 약수 구하기
for i in range(1, N+1):
    if N % i == 0:
        divisor.append(i)
try:
    print(list(divisor)[K - 1])
except:
    print(0)