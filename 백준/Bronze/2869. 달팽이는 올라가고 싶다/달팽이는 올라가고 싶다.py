import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
day = ((V - A) + ((A-B) - 1)) // (A - B) + 1
print(day)

# restDistance = V

# while True:
#     restDistance = restDistance - A
#     if restDistance <= 0:
#         day += 1
#         print(day)
#         break
#     restDistance = restDistance + B
#     day += 1