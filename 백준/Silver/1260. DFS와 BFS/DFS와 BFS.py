from collections import defaultdict, deque

def dfs(start):
    stack = [start]
    visited = [False] * (N+1)
    ans = []

    while stack:
        cur_node = stack.pop()

        if not visited[cur_node]:
            visited[cur_node] = True
            ans.append(cur_node)

            for next_node in reversed(graph[cur_node]):
                if not visited[next_node]:
                    stack.append(next_node)
    return ans

def bfs(start):
    q = deque([start])
    visited = [False] * (N+1)
    ans = []

    while q:
        cur_node = q.popleft()

        if not visited[cur_node]:
            visited[cur_node] = True
            ans.append(cur_node)

            for next_node in graph[cur_node]:
                if not visited[next_node]:
                    q.append(next_node)
    return ans


N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for key in graph:
    graph[key].sort()

print(' '.join(map(str, dfs(V))))
print(' '.join(map(str, bfs(V))))