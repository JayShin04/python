# 카드의 합이 21을 넘지 않는 한도 내에서
# 카드의 합을 최대한 크게 만드는 게임
# N장의 카드를 바닥에 놓고 숫자 M을 크게 외친다.
# N장의 카드 중에서 3장의 카드를 고르고 M과 최대한 가깝게 합을 만들어야한다.
 # M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력

# 입력
# 카드의 개수 N, M
N, M = map(int, input().split())
cardList = list(map(int, input().split()))
cardList.sort(reverse=True)
closeToM = 0
tempSum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tempSum = cardList[i] + cardList[j] + cardList[k]
            if tempSum > M:
                continue
            else:
                if closeToM < tempSum:
                    closeToM = tempSum
print(closeToM)