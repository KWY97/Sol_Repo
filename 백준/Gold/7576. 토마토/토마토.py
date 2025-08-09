from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
q = deque()
max_day = 0

dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i, j, 0])

while q:
    x, y, d = q.popleft()
    max_day = max(max_day, d)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if tomato[nx][ny] != 0:
            continue

        tomato[nx][ny] = 1
        q.append([nx, ny, d+1])

for row in tomato:
    if 0 in row:
        print(-1)
        break
else:
    print(max_day)
