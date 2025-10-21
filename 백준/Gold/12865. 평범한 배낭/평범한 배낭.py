N, K = map(int, input().split())
objs = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (K+1)

# dp[i] = 무게 i를 넘기지 않을 때 얻을 수 있는 최대 가치
for w, v in objs:
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(max(dp))