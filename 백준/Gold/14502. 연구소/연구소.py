import sys
import copy
from collections import deque

input = sys.stdin.readline

def my_bfs():
    queue = deque()
    temp_map = copy.deepcopy(my_map)

    for i in range(N):
        for j in range(M):
            if temp_map[i][j] == 2:
                queue.append([i, j])

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if temp_map[nr][nc] == 0:
                temp_map[nr][nc] = 2
                queue.append([nr, nc])

    global answer
    cnt = 0

    for i in range(N):
        cnt += temp_map[i].count(0)
    answer = max(answer, cnt)

def wall(cnt):
    if cnt == 3:
        my_bfs()
        return

    for i in range(N):
        for j in range(M):
            if my_map[i][j] == 0:
                my_map[i][j] = 1
                wall(cnt+1)
                my_map[i][j] = 0

N, M = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = 0
wall(0)
print(answer)