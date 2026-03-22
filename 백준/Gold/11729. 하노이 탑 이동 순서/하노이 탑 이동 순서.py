# n을 3으로 옮기려면 n-1개의 탑을 2로 옮겨야한다
# 그리고 n을 3으로 옮긴다.
# 그리고 n-1개의 탑을 3으로 옮긴다.
def func(a, b, n):
    # base condition
    if n == 1:
        print(f"{a} {b}")
        return
    func(a, 6-a-b, n-1)
    print(f"{a} {b}")
    func(6-a-b, b, n-1)

k = int(input())
print((1<<k)-1)
func(1, 3, k)
