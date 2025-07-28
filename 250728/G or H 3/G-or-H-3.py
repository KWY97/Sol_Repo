# 사진의 크기: K (양쪽 끝의 x 값 끼리의 차)
# G: 1점, H: 2점
# 사진 찍어 얻을 수 있는 최대 점수

N, K = map(int, input().split())
infos = [0] * 30
max_loc = 0
ans = None

for _ in range(N):
    loc, alphabet = input().split()
    if alphabet == 'G':
        infos[int(loc)] = 1
    elif alphabet == 'H':
        infos[int(loc)] = 2
    max_loc = max(max_loc, int(loc))

for i in range(1, max_loc-K+2):
    temp = 0
    for j in range(i, i+K+1):
        temp += infos[j]
        if ans is None or ans < temp:
            ans = temp

print(ans)