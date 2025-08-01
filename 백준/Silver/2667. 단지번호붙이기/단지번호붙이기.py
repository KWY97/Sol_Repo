from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])
    arr[x][y] = 0
    width = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] == 0:
                continue

            q.append([nx, ny])
            arr[nx][ny] = 0
            width += 1

    if width != 0:
        widths.append(width)
        return 1
    return 0


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0
widths = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += bfs(i, j)

widths.sort()

print(cnt)
print('\n'.join(map(str, widths)))