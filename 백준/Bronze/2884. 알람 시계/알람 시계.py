h, m = map(int, input().split())
alarmH = h
alarmM = m - 45
if alarmM < 0:
  alarmH -= 1
  alarmM = alarmM + 60
if alarmH < 0:
  alarmH = 24 + alarmH
print(str(alarmH) + " " + str(alarmM))