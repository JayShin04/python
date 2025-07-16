word = input()
start = 0
end = len(word)-1
for k in word:
    if k != " ":
        start = word.index(k)
        break
for k in range(len(word)):
    end = len(word) - 1 - k
    if word[end] != " ":
        break

word = word[start:end+1].split()
print(len(word))