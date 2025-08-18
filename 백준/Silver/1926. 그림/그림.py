from collections import deque

def bfs(in_x, in_y):
    q = deque()
    visited[in_x][in_y] = 1
    q.append([in_x, in_y])
    area = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny] or art[nx][ny] == 0:
                continue

            visited[nx][ny] = 1
            q.append([nx, ny])
            area += 1

    return area


N, M = map(int, input().split())
art = [list(map(int, input().split())) for _ in range(N)]
pic_cnt = 0
max_area = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if art[i][j] == 1 and not visited[i][j]:
            pic_cnt += 1
            max_area = max(max_area, bfs(i, j))

print(pic_cnt)
print(max_area)
