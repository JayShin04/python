SIZE = 9

array = []
for _ in range(SIZE):
    array.append(list(map(int, input().split())))

maximum = array[0][0]
pos = [1, 1]

for row in range(SIZE):
    for col in range(SIZE):
        if array[row][col] > maximum:
            maximum = array[row][col]
            pos[0] = row + 1
            pos[1] = col + 1
        elif array[row][col] == maximum:
            if (row + 1) < pos[0]:
                maximum = array[row][col]
                pos[0] = row + 1
                pos[1] = col + 1
            elif (row + 1) == pos[0] and (col + 1) < pos[1]:
                maximum = array[row][col]
                pos[0] = row + 1
                pos[1] = col + 1

print(maximum)
print(pos[0], pos[1])
