angle = [ ]
angle.append(int(input()))
angle.append(int(input()))
angle.append(int(input()))

def twoAngle(angle): 
    flag = False       
    for i in range(len(angle)):
        for j in range(i+1, len(angle)):
            if angle[i] == angle[j]:
                flag = True
                return flag
    return flag
if sum(angle) != 180:
    print("Error")
elif twoAngle(angle):
    if angle[0] == angle[1] and angle[1] == angle[2]:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    print("Scalene")
 