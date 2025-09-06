N = int(input())
#dp[i] = i킬로그램을 배달할 때 최소 봉지 수
dp = [-1] * (N+1)
dp[0] = 0
dp[3] = 1

for i in range(5, N+1):
    best = 1667
    if dp[i-3] != -1:
        best = min(best, dp[i-3] + 1)
    if dp[i-5] != -1:
        best = min(best, dp[i-5] + 1)

    if best == 1667:
        dp[i] = -1
    else:
        dp[i] = best

print(dp[N])
