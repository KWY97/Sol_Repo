from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    move = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    q = deque()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs(ix, iy):
        q.append([ix, iy])
        visited[ix][iy] = 1
        move[ix][iy] = 1

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if visited[nx][ny] == 1:
                    continue

                q.append([nx, ny])
                visited[nx][ny] = 1
                move[nx][ny] = move[x][y] + 1

                if (nx == n - 1) and (ny == m - 1):
                    return move[n - 1][m - 1]
        return -1

    answer = bfs(0, 0)

    return answer