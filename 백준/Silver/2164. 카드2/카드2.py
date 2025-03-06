import sys
input = sys.stdin.readline
from collections import deque
queue = deque()

# leftpop 하고 
# leftpop 한번 더 하고 그걸 append
# 이걸 배열 길이가 1일 때 까지

N = int(input())
for i in range(1, N+1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])