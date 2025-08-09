from collections import deque

def coloring(i1, j1, i2, j2):
    for i in range(i1, i2):
        for j in range(j1, j2):
            board[i][j] = 1

def bfs(ix, iy):
    q.append([ix, iy])
    board[ix][iy] = 2
    width = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if board[nx][ny] != 0:
                continue

            q.append([nx, ny])
            board[nx][ny] = 2
            width += 1

    return width

M, N, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
q = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    coloring(sx, sy, ex, ey)

# 영역의 개수
loc_cnt = 0
# 넓이 리스트
widths = []

for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            continue
        widths.append(bfs(i, j))
        loc_cnt += 1

widths.sort()
print(loc_cnt)
print(*widths)