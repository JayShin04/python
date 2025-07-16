rest = [ ]
for i in range(10):
    a = int(input())
    rest.append(a % 42)

restSet = set(rest)
count = 0
for i in restSet:
    count += 1

print(count)