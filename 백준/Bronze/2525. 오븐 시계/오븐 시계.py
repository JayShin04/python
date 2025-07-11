currentHour, currentMinute = map(int, input().split())
cookTime = int(input())
currentMinute += cookTime
while currentMinute >= 60:
  currentHour += 1
  currentMinute -= 60
if currentHour >= 24:
  currentHour %= 24
print(str(currentHour) + " " + str(currentMinute))