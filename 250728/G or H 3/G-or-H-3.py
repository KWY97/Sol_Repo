# 사진의 크기: K (양쪽 끝의 x 값 끼리의 차)
# G: 1점, H: 2점
# 사진 찍어 얻을 수 있는 최대 점수

N, K = map(int, input().split())
infos = [0] * 40
max_loc = 0
ans = None

for _ in range(N):
    loc, alphabet = input().split()
    infos[int(loc)] = alphabet
    max_loc = max(max_loc, int(loc))

print(infos)

for i in range(max_loc+1):
    if infos[i] != 0:
        temp = 0
        for j in range(i, i+K+1):
            if infos[j] == 'G':
                temp += 1
            elif infos[j] == 'H':
                temp += 2

        if ans is None or ans < temp:
            ans = temp

print(ans)