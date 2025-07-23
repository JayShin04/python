def biggerBool(bigger, triangle):
    boolean = bigger < sum(triangle)
    return boolean
a, b, c = map(int, input().split())
triangle = [a, b, c]
bigger = max(triangle)
triangle.remove(bigger)
while bigger >= 1:
    if biggerBool(bigger, triangle):
        triangle.append(bigger)
        print(sum(triangle))
        break
    else:
        bigger = bigger - 1