#피보나치 수열 재귀로 짜기
#피보나치란? Fn = Fn-1 + Fn-2
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 결과가 F2가 되고, F2가 F1이 되고, 결과는 결국 F1 + f2로 넘어감
def func(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return func(n-2) + func(n-1)

n = int(input())
result = func(n)
print(result)

# func(n) -> 피보나치의 Fn을 알려달라
# func(n-2) + func(n-1) 그 전항과 그 전전항을 더하면 Fn이 나올것