from collections import deque

N, M = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)

target_locs = list(map(int,input().split()))
cnt = 0

for target_loc in target_locs:
    while True:
        if queue[0] == target_loc:
            queue.popleft()
            break
        else:
            if queue.index(target_loc) < len(queue)/2:
                while queue[0] != target_loc:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != target_loc:
                    queue.appendleft(queue.pop())
                    cnt += 1

print(cnt)