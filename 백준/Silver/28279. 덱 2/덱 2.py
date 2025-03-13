from collections import deque

import sys
input = sys.stdin.readline

queue = deque()

N = int(input())

for _ in range(N):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        queue.appendleft(arr[1])
    elif arr[0] == 2:
        queue.append(arr[1])
    elif arr[0] == 3:
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif arr[0] == 4:
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif arr[0] == 5:
        print(len(queue))
    elif arr[0] == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 7:
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif arr[0] == 8:
        if len(queue) != 0:
            print(queue[len(queue)-1])
        else:
            print(-1)