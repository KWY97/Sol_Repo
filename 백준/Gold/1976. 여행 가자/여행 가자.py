def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
adjM = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if adjM[i][j] == 1:
            union(i+1, j+1)

root = find(order[0])
ok = True

for city in order[1:]:
    if find(city) != root:
        ok = False
        break
print("YES" if ok else "NO")