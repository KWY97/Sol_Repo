def cal_distance(li, n):
    ans = 0

    for j in range(n-1):
        ans += abs(li[j][0] - li[j+1][0]) + abs(li[j][1] - li[j+1][1])
    return ans


N = int(input())
cps = [list(map(int, input().split())) for _ in range(N)]
min_dist = None

# 건너뛸 체크 포인트 고르기
for i in range(1, N-1):
    # 선택한 체크 포인트 건너뛰고 계산할 복사본 만들기
    copy_cps = cps[:]
    copy_cps.remove(copy_cps[i])

    # 거리 계산하기
    dist = cal_distance(copy_cps, len(copy_cps))
    if min_dist is None or min_dist > dist:
        min_dist = dist

print(min_dist)