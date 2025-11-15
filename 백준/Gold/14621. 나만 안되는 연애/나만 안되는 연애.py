def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

N, M = map(int, input().split())
gender = list(input().split())
parent = [i for i in range(N+1)]

edge = []
for _ in range(M):
    u, v, d = map(int, input().split())
    if gender[u-1] != gender[v-1]:
        edge.append((d, u, v))
edge.sort()

mst_cost = 0
cnt = 0
for cost, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        mst_cost += cost
        cnt += 1

        if cnt == N-1:
            break

print(mst_cost if cnt == N-1 else -1)