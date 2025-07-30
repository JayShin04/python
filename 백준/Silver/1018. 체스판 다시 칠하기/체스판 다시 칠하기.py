N, M = map(int, input().split())
board = [input() for _ in range(N)]

def count_mismatch(x, y):
    w_start = 0
    b_start = 0
    for i in range(8):
        for j in range(8):
            current = board[x + i][y + j]
            if (i + j) % 2 == 0:
                if current != 'W':
                    w_start += 1
                if current != 'B':
                    b_start += 1
            else:
                if current != 'B':
                    w_start += 1
                if current != 'W':
                    b_start += 1
    return min(w_start, b_start)

min_count = 51
for i in range(N - 7):
    for j in range(M - 7):
        min_count = min(min_count, count_mismatch(i, j))

print(min_count)
