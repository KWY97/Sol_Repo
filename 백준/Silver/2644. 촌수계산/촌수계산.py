def my_dfs(s, depth):
    if s == p2:
        return depth

    visited[s] = 1

    for next in adjL[s]:
        if visited[next] == 0:
            result = my_dfs(next, depth + 1)
            if result != -1:
                return result
    return -1


n = int(input()) # 사람 수
adjL = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

p1, p2 = map(int, input().split()) # 촌수 계산이 필요한 두 사람의 번호
m = int(input()) # 부모 자식들 간의 관계의 개수
for _ in range(m):
    x, y = map(int, input().split())
    adjL[x].append(y)
    adjL[y].append(x)
print(my_dfs(p1, 0))