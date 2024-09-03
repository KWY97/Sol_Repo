import sys
sys.setrecursionlimit(10**5)

def my_dfs(node):
    for i in adjL[node]:
        if parent[i] == 0:
            parent[i] = node
            my_dfs(i)

N = int(input())
adjL = [[] for _ in range(N+1)]
parent = [0] * (N+1)
root = 1
for _ in range(N-1):
    node1, node2 = map(int, input().split())
    adjL[node1].append(node2)
    adjL[node2].append(node1)

my_dfs(root)
ans = parent[2:]
for parent_node in ans:
    print(parent_node)