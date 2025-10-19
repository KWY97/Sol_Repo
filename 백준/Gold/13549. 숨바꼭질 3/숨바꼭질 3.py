import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append(start)

    visited = [False] * 200001
    visited[start] = True

    line = [0] * 200001

    while queue:
        current = queue.popleft()

        if current == end:
            return line[current]

        for next in (current * 2, current - 1, current + 1):
            if 0 <= next <= 200000 and not visited[next]:
                if next == current * 2:
                    line[next] = line[current]
                else:
                    line[next] = line[current] + 1

                queue.append(next) 
                visited[next] = True

N, K = map(int, input().split())
print(bfs(N, K))
