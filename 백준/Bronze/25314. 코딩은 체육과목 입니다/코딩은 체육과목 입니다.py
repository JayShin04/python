n = int(input())
answer = "int"
count = n // 4
for i in range(count):
  answer = "long " + answer
print(answer)