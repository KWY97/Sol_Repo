import heapq
from collections import defaultdict

def dijkstra(start, target):
    dist = [INF] * (n+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_cost, u = heapq.heappop(pq)

        if cur_cost > dist[u]:
            continue

        if u == target:
            return cur_cost

        for v, w in graph[u]:
            next_cost = cur_cost + w
            if next_cost < dist[v]:
                dist[v] = next_cost
                heapq.heappush(pq, (next_cost, v))

    return dist[target]

n, m = map(int, input().split())
graph = defaultdict(list)
INF = int(10e9)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

s, t = map(int, input().split())
ans = dijkstra(s, t)
print(ans)

