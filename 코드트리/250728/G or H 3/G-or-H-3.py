N, K = map(int, input().split())
infos = [0] * 10001
max_loc = 0
ans = None

for _ in range(N):
    loc, alphabet = input().split()
    if alphabet == 'G':
        infos[int(loc)] = 1
    elif alphabet == 'H':
        infos[int(loc)] = 2
    max_loc = max(max_loc, int(loc))

for i in range(1, max(max_loc-K+2, 2)):
    temp = 0
    for j in range(i, i+K+1):
        temp += infos[j]
    if ans is None or ans < temp:
        ans = temp

print(ans)