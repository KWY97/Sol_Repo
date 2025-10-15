import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


def dijkstra(start, finish):
    inf = 10**15
    dist = [inf] * (N+1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_w, cur_v = heapq.heappop(pq)

        if cur_w > dist[cur_v]:
            continue
        if cur_v == finish:
            break

        for w, next_v in graph[cur_v]:
            next_w = cur_w + w
            if dist[next_v] > next_w:
                dist[next_v] = next_w
                heapq.heappush(pq, (next_w, next_v))

    return dist[finish]

N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().strip().split())
    graph[u].append((w, v))

s, f = map(int, input().split())
ans = dijkstra(s, f)
print(ans)