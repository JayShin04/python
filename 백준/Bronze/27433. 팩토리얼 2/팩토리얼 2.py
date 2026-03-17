def get_factorial(x):
    if x > 1:
        return x * get_factorial(x-1)
    else:
        return 1

N = int(input())
print(get_factorial(N))