import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
K = int(input())
INF = 10**15

graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
dist[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

pq = []
heapq.heappush(pq, (0, K))

while pq:
    cur_w, cur_v = heapq.heappop(pq)

    if cur_w > dist[cur_v]:
        continue

    for next_v, w in graph[cur_v]:
        next_w = cur_w + w

        if dist[next_v] > next_w:
            dist[next_v] = next_w
            heapq.heappush(pq, (next_w, next_v))

for x in dist[1:]:
    print(x if x != INF else "INF")