from collections import deque

def bfs(start, target):
    visited = [0] * (N+1)
    visited[start] = 1
    q = deque()
    q.append([start, 0])

    while q:
        cur_node, cur_distance = q.popleft()
        if cur_node == target:
            return cur_distance

        for next_node, next_distance in adjL[cur_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                q.append([next_node, cur_distance + next_distance])

N, M = map(int, input().split())
adjL = [[] for _ in range(N+1)]

for _ in range(N-1):
    node1, node2, d = map(int, input().split())
    adjL[node1].append([node2, d])
    adjL[node2].append([node1, d])

for _ in range(M):
    start_node, target_node = map(int, input().split())
    print(bfs(start_node, target_node))