n = int(input())
cows = [[] for _ in range(n+1)]
cnt = 0

for _ in range(n):
    # position: 왼쪽 -> 0, 오른쪽 -> 1
    cow, position = map(int, input().split())
    cows[cow].append(position)

for cow in cows:
    if not cow:
        continue
    if len(cow) == 1:
        continue
    for i in range(len(cow)-1):
        if cow[i] != cow[i+1]:
            cnt += 1

print(cnt)