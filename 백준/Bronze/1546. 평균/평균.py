N = int(input())
scores = list(map(int, input().split()))
maxScore = max(scores)
calculateScore = [ ]
for i in range(N):
    calculateScore.append(scores[i] / maxScore * 100)
sum = 0
for score in calculateScore:
    sum += score

average = sum / N
print(average)