from collections import deque

def bfs(in_x, in_y, in_cnt):
    q = deque()
    q.append([in_x, in_y, in_cnt])
    visited[in_x][in_y] = 1

    while q:
        x, y, cnt = q.popleft()

        if x == e_i and y == e_j:
            return cnt

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 1:
                continue

            q.append([nx, ny, cnt+1])
            visited[nx][ny] = 1

T = int(input())
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

for _ in range(T):
    n = int(input())
    s_i, s_j = map(int, input().split())
    e_i, e_j = map(int, input().split())
    visited = [[0] * n for _ in range(n)]

    ans = bfs(s_i, s_j, 0)
    print(ans)