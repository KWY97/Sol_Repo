from collections import deque

def dfs(v):
    visited = [False] * (N + 1)
    stack = []
    stack.append(v)
    dfs_ans = []

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = True
            dfs_ans.append(v)

            for next_v in sorted(graph[v], reverse=True):
                if not visited[next_v]:
                    stack.append(next_v)

    return dfs_ans


def bfs(v):
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(v)
    visited[v] = True
    bfs_ans = []

    while queue:
        v = queue.popleft()
        bfs_ans.append(v)

        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

    return bfs_ans

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for lst in graph:
    lst.sort()



print(' '.join(map(str, dfs(V))))
print(' '.join(map(str, bfs(V))))