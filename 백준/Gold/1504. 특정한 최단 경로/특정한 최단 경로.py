import heapq


def dijkstra(start, target):
    dist = [INF] * (N + 1)
    dist[start] = 0
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
    return INF

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = 1e9

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

a, b = map(int, input().split())

path1 = dijkstra(1, a) + dijkstra(a, b) + dijkstra(b, N)
path2 = dijkstra(1, b) + dijkstra(b, a) + dijkstra(a, N)

ans = min(path1, path2)
print(ans if ans < INF else -1)