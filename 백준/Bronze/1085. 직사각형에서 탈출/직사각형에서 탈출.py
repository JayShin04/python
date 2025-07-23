x, y, w, h = map(int, input().split())
minDistance = 1001
if x < w - x:
    minDistance = x
if x >= w - x and minDistance >= w - x:
    minDistance = w - x
if y < h - y and minDistance >= y:
    minDistance = y
if y >= h - y and minDistance >= h - y:
    minDistance = h - y

print(minDistance)