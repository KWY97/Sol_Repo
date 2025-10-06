from collections import deque

def bfs(in_v):
    q.append(in_v)
    d[in_v] = 0

    while q:
        v = q.popleft()

        for nxt_v in adjL[v]:
            if d[nxt_v] != -1:
                continue
            d[nxt_v] = d[v] + 1
            q.append(nxt_v)


N, M = map(int, input().split())
adjL = [[] for _ in range(N+1)]
d = [-1] * (N+1)

q = deque()

for _ in range(M):
    A, B = map(int, input().split())
    adjL[A].append(B)
    adjL[B].append(A)

bfs(1)

room_d = max(d)
equal_room_d = 0
room_n = 0

for i, v in enumerate(d):
    if v == room_d:
        equal_room_d += 1
        if room_n == 0:
            room_n = i

print(room_n, room_d, equal_room_d)