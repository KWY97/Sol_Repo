import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    if moves[x][y] != 0:
        return moves[x][y]

    cur_eat = forest[x][y]
    best = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if cur_eat >= forest[nx][ny]:
            continue
        best = max(best, 1 + dfs(nx, ny))
    moves[x][y] = best
    return best

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
moves = [[0] * N for _ in range(N)]
ans = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))

print(ans)