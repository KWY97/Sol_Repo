import heapq
from collections import defaultdict

def dijkstra(start):
    dist = [INF] * (N+1)
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if dist[cur_node] < cur_cost:
            continue

        for next_node, cost in graph[cur_node]:
            next_cost = cur_cost + cost
            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))

    return dist[N]


N, M = map(int, input().split())
graph = defaultdict(list)
INF = int(10e9)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

ans = dijkstra(1)
print(ans)