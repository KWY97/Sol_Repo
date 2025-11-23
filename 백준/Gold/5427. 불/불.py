import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs_fire():
    global board, fire_q, h, w
    size = len(fire_q)
    for _ in range(size):
        x, y = fire_q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            if board[nx][ny] == '#' or board[nx][ny] == '*':
                continue

            board[nx][ny] = '*'
            fire_q.append((nx, ny))


def bfs_escape(sx, sy):
    global board, h, w

    q = deque()
    q.append((sx, sy))
    visited = [[-1] * w for _ in range(h)]
    visited[sx][sy] = 0

    while q:
        bfs_fire()

        size = len(q)
        for _ in range(size):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    return visited[x][y] + 1
                
                if visited[nx][ny] != -1:
                    continue

                if board[nx][ny] != '.':
                    continue

                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return "IMPOSSIBLE"

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    board = []
    fire_q = deque()
    sx = sy = -1

    for i in range(h):
        row = list(input().strip())
        for j in range(w):
            if row[j] == '@':
                sx, sy = i, j
                row[j] = '.'
            elif row[j] == '*':
                fire_q.append((i, j))
        board.append(row)

    ans = bfs_escape(sx, sy)
    print(ans)
