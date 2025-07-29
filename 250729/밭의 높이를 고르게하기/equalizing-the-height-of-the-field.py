N, H, T = map(int, input().split())
heights = list(map(int, input().split()))
min_cost = None

# 시작점 잡기
for i in range(N-T+1):
    cost = 0
    # 구간 잡기
    for j in range(i, i+T):
        # 구간 내 높이 비교
        diff = abs(heights[j]-H)
        if diff != 0:
            cost += diff

    # 최소 비용 구하기
    if min_cost is None or min_cost > cost:
        min_cost = cost

print(min_cost)