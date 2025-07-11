t = int(input())
for i in range(t):
  num1, num2 = map(int, input().split())
  print("Case #" + str(i + 1) + ": " + str(num1), "+",num2,"=",num1 + num2)