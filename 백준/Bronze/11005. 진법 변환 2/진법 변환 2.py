from collections import deque

N, B = map(int, input().split())
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
queue = deque()

while N >= B:
    queue.appendleft(num[N % B])
    N //= B
queue.appendleft(num[N])

ans = list(queue)
print("".join(ans))