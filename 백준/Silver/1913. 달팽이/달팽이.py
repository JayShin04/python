# N 입력하면
# N * N의 표가 만들어지며
# N * N의 표에서 중앙엔 1이 시작되고
# 윗칸 + 달팽이 모양으로 순서대로 값을 채워나감
# N == 3
# 3 * 3 == 9
# 9 2 3
# 8 1 4
# 7 6 5

N = int(input())
findNumber = int(input())

row = N // 2
col = N // 2
table = [[0 for i in range(N)] for j in range(N)]
def printTable(table):
    for eachTable in table:
        for eachTable2 in eachTable:
            print(eachTable2, end=' ')
        print()
table[row][col] = 1

# 반복없이 일반화없이 
# N == 3

number = 2
diffRow = [-1, 0, 1, 0] # 4칸이 순서대로 계속 반복. 
#(diffRow + 1) % 4로 가능할듯
diffCol = [0, 1, 0, -1]

# 반복하는 칸 수
repeatCount = 1
direction = 0
# 1 -> 2 == 1칸이동
# 2 -> 3 == 1칸이동
# 3 -> 5 == 2칸이동
# 5 -> 7 == 2칸이동
# 7 -> 10 == 3칸이동
# 10 -> 13 == 3칸이동
# 13 -> 17 == 4칸이동
# 17 -> 21 == 4칸이동

# 만약 N이 7이라면
# 21 -> 26 == 5칸이동
# 26 -> 31 == 5칸이동
# 31 -> 37 == 6칸이동

# repeatCount가 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, ...
while number <= N * N:
    for i in range(2):
        for j in range(repeatCount):
            row += diffRow[direction]
            col += diffCol[direction]
            if 0 <= row and row < N and 0 <= col and col < N:
                table[row][col] = number
                number += 1
        direction = (direction + 1) % 4
    repeatCount += 1

printTable(table)

for i in range(len(table)):
    try:
        print((i+1),(table[i].index(findNumber)+1))
    except:
        print("",end='')