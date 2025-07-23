N = int(input())
distance = 1
max_number = 1

while N > max_number:
    max_number += 6 * distance
    distance += 1
print(distance)