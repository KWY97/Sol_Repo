from collections import deque

def my_bfs(N):
    queue = deque()
    queue.append([0, 0])
    visited[0] = True

    while queue:
        sum, cnt_bag = queue.popleft() # 현재합, 봉지 수

        if sum == N:
            return cnt_bag

        next_sum = sum + 3
        if next_sum <= N and visited[next_sum] == 0:
            visited[next_sum] = 1
            queue.append([next_sum, cnt_bag + 1])

        next_sum = sum + 5
        if next_sum <= N and visited[next_sum] == 0:
            visited[next_sum] = 1
            queue.append([next_sum, cnt_bag + 1])

    return -1

N = int(input())
visited = [0] * (N + 1)
print(my_bfs(N))