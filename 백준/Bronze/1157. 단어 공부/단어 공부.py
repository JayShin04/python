S = input().upper()
SList = list(set(S))
answerList = [ ]
for k in SList:
    answerList.append(S.count(k))

if answerList.count(max(answerList)) >= 2:
    print("?")
else:
    print(SList[answerList.index(max(answerList))])