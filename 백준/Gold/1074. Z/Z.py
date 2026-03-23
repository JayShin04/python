# n이 1이라하면 2행 2열까지만 있음
# n이 2라하면 4행 4열까지만 있음
# n이 3이라 하면 8행 8열까지만 있음
# n이 k라하면 2^k행 2^k열 까지만 있음

# 0 1 2 3 왼쪽위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
def func(n, r, c):
  if n == 0:
    return 0
  # if r == 0 and c == 0:
  #   return 0
  # elif r == 0 and c == 1:
  #   return 1
  # elif r == 1 and c == 0:
  #   return 2
  # elif r == 1 and c == 1:
  #   return 3
  half = n // 2 # n == 3이라 가정 -> n // 2 = 1 말이안되는데?
  # n == 1일때 2 * 2 이니 반은 1으로 가정
  # n == 2일때 4 * 4 이니 반은 2로 가정
  # n == 3일때 8 * 8 이니 반은 4으로 가정
  # n == 4일때 16 * 16 이니 반은 8로 가정
  # n == k일때 2^k * 2^k 이니 반은 (2^k)/2 -> 2^(k-1)로 가정
  half = 1<<(n-1)
  if r < half and c < half:
    return func(n-1, r, c)
  elif r < half and c >= half:
    return half * half + func(n-1, r, c-half)
  elif r >= half and c < half:
    return 2 * half * half + func(n-1, r-half, c)
  else:
    return 3 * half * half + func(n-1, r-half, c-half)
  
# n = int(input())
# r = int(input())
# c = int(input())
n, r, c = map(int, input().split())
result = func(n, r, c)
print(result)