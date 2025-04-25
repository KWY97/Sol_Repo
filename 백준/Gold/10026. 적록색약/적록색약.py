import sys
from collections import deque

input = sys.stdin.readline

def my_bfs(x, y):
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            # 범위, 방문 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == 1:
                continue
            # 같은 색인지 조건 체크
            if arr[x][y] != arr[nx][ny]:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny))
    
    
n = int(input())
arr = [list(input()) for _ in range(n)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
q = deque()

# 일반반
visited = [[0] * n for _ in range(n)]
result_1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            my_bfs(i,j)
            result_1 += 1

# 적록 색맥용 arr 재구성
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[0] * n for _ in range(n)]
result_2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            my_bfs(i,j)
            result_2 += 1

print(result_1, result_2)