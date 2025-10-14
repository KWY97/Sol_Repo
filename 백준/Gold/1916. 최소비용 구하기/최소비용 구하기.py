import heapq

INF = 10**15
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, finish = map(int, input().split())

dist = [INF] * (N+1)
dist[start] = 0

pq = []
heapq.heappush(pq, (0, start))

while pq:
    cur_w, cur_v = heapq.heappop(pq)
    if cur_w > dist[cur_v]:
        continue
        
    if cur_v == finish:
        break

    for next_v, w in graph[cur_v]:
        next_w = cur_w + w

        if next_w < dist[next_v]:
            dist[next_v] = next_w
            heapq.heappush(pq, (next_w, next_v))

print(dist[finish])