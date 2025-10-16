N = int(input())
adjM = [list(map(int, input().split())) for _ in range(N)]

def dfs(start):
    visited = [0] * N
    stack = [start]

    while stack:
        u = stack.pop()
        for v in range(N):
            if adjM[u][v] == 1 and visited[v] == 0:
                visited[v] = 1
                stack.append(v)
    return visited

for i in range(N):
    print(*dfs(i))