import sys
input = sys.stdin.readline

from collections import deque

K = int(input())
deq = deque()

for _ in range(K):
    num = int(input())

    if num != 0:
        deq.append(num)
    else:
        deq.pop()

print(sum(deq))