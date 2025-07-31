N, H, T = map(int, input().split())
heights = list(map(int, input().split()))
# 초기 값 설정
cost = sum(abs(height-H) for height in heights[:T])
min_cost = cost

for i in range(T, N):
    # 새로운 비용 추가
    cost += abs(heights[i]-H)
    # 이전 값 제거
    cost -= abs(heights[i-T]-H)

    if min_cost > cost:
        min_cost = cost

print(min_cost)