from collections import deque

def catch_me(start, target):
    MAX = 100000
    time_to = [-1] * (MAX + 1)
    path_count = [0] * (MAX + 1)

    q = deque([start])
    time_to[start] = 0
    path_count[start] = 1

    while q:
        x = q.popleft()
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX:
                if time_to[nx] == -1:
                    time_to[nx] = time_to[x] + 1
                    path_count[nx] = path_count[x]
                    q.append(nx)
                elif time_to[nx] == time_to[x] + 1:
                    path_count[nx] += path_count[x]

    return time_to[target], path_count[target]


N, K = map(int, input().split())
t, cnt = catch_me(N, K)
print(t)
print(cnt)
