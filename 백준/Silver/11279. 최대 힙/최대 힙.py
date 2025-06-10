import sys
input = sys.stdin.readline

from heapq import heappop, heappush
max_heapq = []

n = int(input())
for _ in range(n):
    x = int(input())

    if x == 0:
        if not max_heapq:
            print(0)
        else:
            print(-heappop(max_heapq))
    else:
        heappush(max_heapq, -x)