def dfs(u, depth):
    if depth == 2:
        return

    for v in adjL[u]:
        nd = depth + 1
        if dist[v] == -1 or nd < dist[v]:
            dist[v] = nd
            dfs(v, nd)

N = int(input())
M = int(input())
adjL = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjL[a].append(b)
    adjL[b].append(a)

dist = [-1] * (N+1)
dist[1] = 0
dfs(1, 0)

ans = sum(1 for i in range(2, N+1) if 1 <= dist[i] <= 2)
print(ans)