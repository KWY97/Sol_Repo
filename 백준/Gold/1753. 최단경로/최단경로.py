import sys
input = sys.stdin.readline

import heapq
from collections import defaultdict

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

costs = {}
pq = []
heapq.heappush(pq, (0, K))

while pq:
    cur_w, cur_v = heapq.heappop(pq)
    if cur_v not in costs:
        costs[cur_v] = cur_w

        for w, next_v in graph[cur_v]:
            next_w = cur_w + w
            heapq.heappush(pq, (next_w, next_v))

for i in range(1, V+1):
    if i in costs:
        print(costs[i])
    else:
        print('INF')
