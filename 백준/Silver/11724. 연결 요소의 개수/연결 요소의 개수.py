import sys
input = sys.stdin.readline

def f(n):
    global ans

    stack = []

    component = []
    stack.append(n)

    while stack:
        node = stack.pop()

        if visited[node]:
            continue

        visited[node] = True
        component.append(node)

        for next_node in graph[node]:
            if visited[next_node]:
                continue

            stack.append(next_node)
    ans.append(component)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        f(i)
print(len(ans))