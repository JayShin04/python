# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 
# 크기 N의 패턴은 N×N 정사각형 모양이다.

# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

# ***
# * *
# ***

# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 
# 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

# 입력
# 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3^k이며, 이때 1 ≤ k < 8이다.

N = int(input())
board = [[' ' for _ in range(N)] for _ in range(N)]

def func(n, r, c):
    if n == 3:
      for i in range(3):
        for j in range(3):
          if i == 0 or i == 2:        # 첫째줄, 마지막줄
            board[r+i][c+j] = '*'
          elif j == 0 or j == 2:      # 가운데줄 양 끝
            board[r+i][c+j] = '*'
      return
    
    size = n // 3
    for dr in range(3):
        for dc in range(3):
            if dr == 1 and dc == 1:
                continue
            func(size, r + dr*size, c + dc*size)

func(N, 0, 0)
for r in board:
  print(''.join(r))