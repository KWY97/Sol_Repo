import sys
from collections import deque

input = sys.stdin.readline

def bfs(ix, iy):
    q.append([ix, iy])
    ans[ix][iy] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] != 1:
                continue
            if ans[nx][ny] != 0:
                continue

            q.append([nx, ny])
            ans[nx][ny] = ans[x][y] + 1
    return

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * m for _ in range(n)]
q = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

found = False
for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            bfs(i, j)
            found = True
            break
    if found:
        break

for i in range(n):
    for j in range(m):
        if maze[i][j] == 1 and ans[i][j] == 0:
            ans[i][j] = -1

for row in ans:
    print(' '.join(map(str, row)))