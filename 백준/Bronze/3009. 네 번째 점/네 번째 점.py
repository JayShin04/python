rectanglePos = [ ]
rectanglePos.append(list(map(int, input().split())))
rectanglePos[0].append(False)
rectanglePos.append(list(map(int, input().split())))
rectanglePos[1].append(False)
rectanglePos.append(list(map(int, input().split())))
rectanglePos[2].append(False)

for i in range(len(rectanglePos)):
    tempXPos = rectanglePos[i][0]
    for j in range(i+1, len(rectanglePos)):
        if tempXPos == rectanglePos[j][0]:
            rectanglePos[i][2] = True
            rectanglePos[j][2] = True
            break
    if rectanglePos[i][2] == True:
        break

resultPos = []

for i in range(len(rectanglePos)):
    if rectanglePos[i][2] == False:
        resultPos.append(rectanglePos[i][0])
    else:
        rectanglePos[i][2] = False
for i in range(len(rectanglePos)):
    tempYPos = rectanglePos[i][1]
    for j in range(i+1, len(rectanglePos)):
        if tempYPos == rectanglePos[j][1]:
            rectanglePos[i][2] = True
            rectanglePos[j][2] = True
            break
    if rectanglePos[i][2] == True:
        break

for i in range(len(rectanglePos)):
    if rectanglePos[i][2] == False:
        resultPos.append(rectanglePos[i][1])

for pos in resultPos:
    print(pos, end=' ')