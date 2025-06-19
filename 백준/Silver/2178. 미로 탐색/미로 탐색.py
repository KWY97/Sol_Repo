from collections import deque

def bfs(r, c):
    queue = deque()
    queue.append([r, c])
    dist = [[0] * M for _ in range(N)]
    dist[0][0] = 1

    while queue:
        r, c = queue.popleft()
        if r == N-1 and c == M-1:
            return dist[r][c]

        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]

            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M or my_map[next_r][next_c] == 0:
                continue

            if dist[next_r][next_c] != 0:
                continue

            dist[next_r][next_c] = dist[r][c] + 1
            queue.append([next_r, next_c])

N, M = map(int, input().split())
my_map = [list(map(int, input())) for _ in range(N)]
# (0, 0) -> (N-1, M-1)로 이동
# 0은 벽, 1은 갈 수 있다.
# 지나야 하는 최소칸의 수 구하는 프로그램
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print(bfs(0, 0))