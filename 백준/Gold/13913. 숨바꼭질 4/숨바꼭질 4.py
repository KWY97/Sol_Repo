import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    q = deque([start])
    dist[start] = 0

    while q:
        cur = q.popleft()
        if cur == end:
            return dist[cur]

        nxt = cur * 2
        if 0 <= nxt < MAX and dist[nxt] > dist[cur] + 1:
            dist[nxt] = dist[cur] + 1
            prev[nxt] = cur
            q.appendleft(nxt)

        nxt = cur - 1
        if 0 <= nxt < MAX and dist[nxt] > dist[cur] + 1:
            dist[nxt] = dist[cur] + 1
            prev[nxt] = cur
            q.append(nxt)

        nxt = cur + 1
        if 0 <= nxt < MAX and dist[nxt] > dist[cur] + 1:
            dist[nxt] = dist[cur] + 1
            prev[nxt] = cur
            q.append(nxt)


    return dist[end]


N, K = map(int, input().split())
INF = 10**15
MAX = 200001
dist = [INF] * MAX
prev = [-1] * MAX
print(bfs(N, K))

path = []
s = K
while s != -1:
    path.append(s)
    s = prev[s]
path.reverse()

print(*path)