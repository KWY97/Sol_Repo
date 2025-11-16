import sys, heapq
input = sys.stdin.readline

def dijkstra(s):
    dist = [INF] * (n+1)
    dist[s] = 0
    prev = [-1] * (n + 1)

    pq = []
    heapq.heappush(pq, (0, s))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if dist[cur_node] < cur_cost:
            continue

        for next_node, cost in graph[cur_node]:
            next_cost = cur_cost + cost

            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                prev[next_node] = cur_node
                heapq.heappush(pq, (next_cost, next_node))
    return dist, prev

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e12)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, target = map(int, input().split())
dist, prev = dijkstra(start)

ans1 = dist[target]

path = []
cur = target
while cur != -1:
    path.append(cur)
    cur = prev[cur]

path.reverse()
ans2 = len(path)
ans3 = ' '.join(map(str, path))

print(ans1)
print(ans2)
print(ans3)