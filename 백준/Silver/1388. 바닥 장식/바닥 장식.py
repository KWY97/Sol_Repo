N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
cnt = 0

# 행 기준 검사
for i in range(N):
    for j in range(M):
        if board[i][j] == '-':
            if j == 0:
                cnt += 1
            else:
                if board[i][j-1] != '-':
                    cnt += 1



# 열 기준 검사
for i in range(M):
    for j in range(N):
        if board[j][i] == '|':
            if j == 0:
                cnt += 1
            else:
                if board[j-1][i] != '|':
                    cnt += 1

print(cnt)