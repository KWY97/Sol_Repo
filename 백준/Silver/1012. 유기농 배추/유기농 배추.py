# 4 방향으로 1로 뭉쳐진 구역이 몇 개 인지 구하시오.

import sys
from collections import deque
input = sys.stdin.readline

def my_bfs(si, sj):
    queue.append([si, sj])
    field[si][sj] = 2

    while queue:
        ni, nj = queue.popleft()

        for dx, dy in dxy:
            nx = ni + dx
            ny = nj + dy

            # 범위 체크
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                continue

            # 현 위치에 배추가 있는지 확인
            if field[nx][ny] == 0:
                continue

            # 구역으로 카운트한 배추라면 탐색 X
            if field[nx][ny] == 2:
                continue

            queue.append([nx, ny])
            field[nx][ny] = 2
    return 1


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * (M) for _ in range(N)]
    queue = deque()

    for _ in range(K):
        x, y = map(int, input().split()) # 배추가 심어져 있는 위치
        field[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                cnt += my_bfs(i, j)

    print(cnt)