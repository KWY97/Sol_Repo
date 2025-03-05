import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
stack = []

for _ in range(N):
    arr = list(map(int, input().split()))
    
    if arr[0] == 1:
        stack.append(arr[1])
    elif arr[0] == 2:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif arr[0] == 3:
        print(len(stack))
    elif arr[0] == 4:
        if (len(stack) == 0):
            print(1)
        else:
            print(0)
    elif arr[0] == 5:
        if (len(stack) != 0):
            print(stack[-1])
        else:
            print(-1)

