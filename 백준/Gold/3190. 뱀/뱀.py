from collections import deque

def isThereAnApple(row, col, board, apple):
    return board[row][col] == apple
def isThereSnakeBody(row, col, board, snake):
    return board[row][col] == snake
def areRowAndColInRange(row, col, board):
    return 0 <= row and row < len(board) and 0 <= col and col < len(board)
def printBoard(board, snake):
    for i in range(len(snake)):
        board[snake[i][0]][snake[i][1]] = 1
    for each in board:
        print(each)
    
N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
apple = -1

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = apple

L = int(input())
tilt = deque()
for _ in range(L):
    X, C = input().split()
    X = int(X)
    tilt.append([X, C])

snake = deque()
snake.append([0, 0])
row, col = 0, 0

# 위 오른쪽 아래 왼쪽
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]
currentDirection = 1  # 처음엔 오른쪽

time = 0
while True:
    time += 1
    newRow = row + dRow[currentDirection]
    newCol = col + dCol[currentDirection]

    if not areRowAndColInRange(newRow, newCol, board) or [newRow, newCol] in snake:
        break

    snake.append([newRow, newCol])
    if isThereAnApple(newRow, newCol, board, apple):
        board[newRow][newCol] = 0  # 사과 먹음, 꼬리 안 줄임
    else:
        snake.popleft()

    if tilt and tilt[0][0] == time:
        i, directionChar = tilt.popleft()
        if directionChar == 'L':
            currentDirection = (currentDirection - 1) % 4
        elif directionChar == 'D':
            currentDirection = (currentDirection + 1) % 4
    row, col = newRow, newCol
# printBoard(board, snake)
print(time)
