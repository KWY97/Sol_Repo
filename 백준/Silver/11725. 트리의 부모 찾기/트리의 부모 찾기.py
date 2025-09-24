from collections import deque

def bfs(root_node):
    q = deque([root_node])
    parent[root_node] = -1

    while q:
        cur = q.popleft()
        for next_node in adjL[cur]:
            if parent[next_node] == 0:
                parent[next_node] = cur
                q.append(next_node)

N = int(input())
adjL = [[] for _ in range(N+1)]
parent = [0] * (N+1)
root = 1

for _ in range(N-1):
    a, b = map(int, input().split())
    adjL[a].append(b)
    adjL[b].append(a)

bfs(root)
print('\n'.join(map(str, parent[2:])))