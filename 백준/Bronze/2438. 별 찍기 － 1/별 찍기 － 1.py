scan = int(input())
answer = ""
for i in range(1, scan+1):
  for j in range(1, i+1):
    answer = "*" * j
  print(answer)