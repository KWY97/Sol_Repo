from collections import deque, defaultdict

def bfs(start):
    dist = [-1] * (N+1)
    q = deque([start])
    dist[start] = 0

    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return sum(dist[1:])

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = [0] * (N+1)
for i in range(1, N+1):
    ans[i] = bfs(i)

print(ans.index(min(ans[1:])))
