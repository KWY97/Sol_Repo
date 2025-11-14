import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

def dijkstra(start, target):
    dist = [INF] * (n+1)
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_w, cur_v = heapq.heappop(pq)

        if dist[cur_v] < cur_w:
            continue

        if cur_v == target:
            return cur_w

        for next_v, w in graph[cur_v]:
            next_w = cur_w + w

            if dist[next_v] > next_w:
                dist[next_v] = next_w
                heapq.heappush(pq, (next_w, next_v))
    return dist[target]

n, m = map(int, input().split())
graph = defaultdict(list)
INF = int(10e9)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

s, t = map(int, input().split())

print(dijkstra(s, t))