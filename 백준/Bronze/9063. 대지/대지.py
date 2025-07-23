N = int(input())
dotPos = []
for _ in range(N):
    x, y = map(int, input().split())
    dotPos.append([x, y])
xPosArray = []
for i in range(len(dotPos)):
    xPosArray.append(dotPos[i][0])

yPosArray = []
for i in range(len(dotPos)):
    yPosArray.append(dotPos[i][1])

oneLength = max(xPosArray) - min(xPosArray)
firstPos = [min(xPosArray), min(yPosArray)]
lastPos = [max(xPosArray), max(yPosArray)]
area = (lastPos[0] - firstPos[0]) * (lastPos[1]-firstPos[1])
print(area)