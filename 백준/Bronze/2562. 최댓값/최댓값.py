numberArray = [ ]
for i in range(9):
    numberArray.append(int(input()))

maximum = max(numberArray)
index = numberArray.index(maximum)
print(maximum)
print(index + 1)