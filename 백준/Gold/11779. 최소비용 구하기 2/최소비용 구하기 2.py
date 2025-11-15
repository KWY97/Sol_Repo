import heapq
from collections import defaultdict


def dijkstra(s, t):
    dist = [INF] * (n+1)
    dist[s] = 0
    prev = [0] * (n+1)
    pq = []
    heapq.heappush(pq, (0, s))

    while pq:
        cur_w, cur_v = heapq.heappop(pq)

        if dist[cur_v] < cur_w:
            continue

        for next_v, w in graph[cur_v]:
            next_w = cur_w + w

            if dist[next_v] > next_w:
                dist[next_v] = next_w
                prev[next_v] = cur_v
                heapq.heappush(pq, (next_w, next_v))

    return dist[t], prev


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e12)
route = []

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, target = map(int, input().split())
ans1, prev = dijkstra(start, target)

path = []
cur = target
while cur != 0:
    path.append(cur)
    cur = prev[cur]
path.reverse()

ans2 = len(path)
ans3 = (' '.join(map(str, path)))

print(ans1)
print(ans2)
print(ans3)