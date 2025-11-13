import heapq
from collections import defaultdict

def dijkstra(graph, start, target):
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost

            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))

    return costs[target]

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

print(dijkstra(graph, 1, N))
