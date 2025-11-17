import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]

ans = 0
cnt = 0

for _ in range(E):
    u, v, c = map(int, input().split())
    edges.append((c, u, v))

edges.sort()

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost
        cnt += 1

        if cnt == V - 1:
            break

print(ans)