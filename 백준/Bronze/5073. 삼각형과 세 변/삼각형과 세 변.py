def twoSide(triangle):
    flag = False
    for i in range(len(triangle)):
        for j in range(i+1, len(triangle)):
            if triangle[i] == triangle[j]:
                flag = True
                return flag
    return flag

while True:
    q, r, s = map(int, input().split())
    if q == 0 and r == 0 and s == 0:
        break
    triangle = [q, r, s]
    bigger = max(triangle)
    triangle.remove(bigger)
    if bigger >= triangle[0] + triangle[1]:
        print("Invalid")
        continue
    
    triangle.append(bigger)
    
    if triangle[0] == triangle[1] and triangle[1] == triangle[2]:
        print("Equilateral")
    elif twoSide(triangle):
        print("Isosceles")
    else:
        print("Scalene")