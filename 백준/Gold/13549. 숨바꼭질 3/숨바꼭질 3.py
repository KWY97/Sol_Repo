import sys
input = sys.stdin.readline

from collections import deque

def my_bfs(start, end):
    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.popleft()

        if current == end:
            return line[current]
        
        for next in [current * 2, current - 1, current + 1]:

            if next < 0 or next >= 200001 or visited[next] != -1:
                continue

            if next == current * 2:
                line[next] = line[current]
            else:
                line[next] = line[current] + 1

            queue.append(next)
            visited[next] = visited[current] + 1


N, K = map(int, input().split())
visited = [-1] * 2000001
line = [0] * 200001
queue = deque()


print(my_bfs(N, K))