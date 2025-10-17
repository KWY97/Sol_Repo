import heapq

def dijkstra(start, target):
    pq = []
    heapq.heappush(pq, (0, start))
    dist = [INF] * (N + 1)
    dist[start] = 0

    while pq:
        cur_w, cur_v = heapq.heappop(pq)
        if cur_w > dist[cur_v]:
            continue

        if cur_v == target:
            return dist[cur_v]

        for next_v, w in graph[cur_v]:
            next_w = cur_w + w
            if next_w < dist[next_v]:
                dist[next_v] = next_w
                heapq.heappush(pq, (next_w, next_v))



N, M, X = map(int, input().split())
INF = 10**15
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

ans = [0] * (N+1)
b = 0

for i in range(1, N+1):
    # i -> X 가는 다익스트라
    ans[i] += dijkstra(i, X)
    # X -> i 가는 다익스트라
    ans[i] += dijkstra(X, i)

cand = [a for a in ans[1:] if a < INF]
print(max(cand))