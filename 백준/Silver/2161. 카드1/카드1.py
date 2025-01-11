from collections import deque

N = int(input())
cards = deque()
result = []

for i in range(1, N+1):
    cards.append(i)

while True:
    result.append(cards.popleft())
    if not cards:
        break
    cards.append(cards.popleft())

print(*result)