N = int(input())
groupWordCount = 0
for i in range(N):
    word = input()
    duplicatedWords = set()
    isGroupWord = True
    previousWord = ''

    for c in word:
        if c in duplicatedWords:
            if c != previousWord:
                isGroupWord = False
                break
        else:
            duplicatedWords.add(c)
        previousWord = c
    if isGroupWord:
        groupWordCount += 1
print(groupWordCount)