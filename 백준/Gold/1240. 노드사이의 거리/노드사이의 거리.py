from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, target):
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([(start, 0)])

    while q:
        node, dist = q.popleft()
        if node == target:
            return dist

        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, dist + weight))

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

for _ in range(M):
    u, v = map(int, input().split())
    print(bfs(u, v))
