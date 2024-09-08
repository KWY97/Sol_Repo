import sys
sys.setrecursionlimit(10**5)

def my_bfs(s):
    # visited를 바꾸는데 리스트는 함수안에서 원본이 바뀌므로 굳이 return X
    global num
    visited[s] = num
    num += 1

    for next in adjL[s]:
        if visited[next] == 0: # 방문하지 않았다면
            my_bfs(next) # 그 정점으로 가서 탐색 시작

N, M, R = map(int, input().split())
adjL = [[] for _ in range(N+1)]
visited = [0] * (N+1)
num = 1

# 정점의 수, 간선의 수, 시작 정점
for _ in range(M):
    u, v = map(int, input().split())
    adjL[u].append(v)
    adjL[v].append(u)

for i in range(N+1):
    adjL[i].sort()

my_bfs(R)

for v in range(1, N+1):
    print(visited[v])