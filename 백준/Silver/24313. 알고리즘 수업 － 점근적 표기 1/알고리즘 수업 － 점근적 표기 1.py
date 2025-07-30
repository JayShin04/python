# O(g(n)) = {f(n) | 모든 n >= N에 대하여 
#           f(n) <= c * g(n)인 양의 상수 c와 N이 존재한다}
# 함수 f(n) = an + b 양의 정수 c, N이 주어질 경우 O(n) 정의를 만족하는지

#입력
# 첫째쭐 f(n) = an + b에서 a, b가 주어진다.
# 다음줄 양의정수 c가 주어진다.
# 다음줄 양의정수 N이 주어진다.

#출력
# f(n), c, N이 O(n)의 정의를 만족하면 1, 아니면 0을 출력한다.
# f(n) <= c * g(n) 만족해야함
# n >= N에 대하여 이므로 이것도 만족해야함

a, b = map(int, input().split())
c = int(input())
N = int(input())
isTrue = True
for random_Number in range(N, 101): 
    function_N = a * random_Number + b
    g_N = random_Number
    function_A = c * g_N
    if not(function_N <= c * g_N and random_Number >= N):
        print(0)
        isTrue = False
        break
if isTrue:
    print(1)