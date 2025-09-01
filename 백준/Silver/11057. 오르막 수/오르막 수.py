N = int(input())
dp = [[0] * 10 for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for d in range(10):
        total = 0
        for k in range(d+1):
            total += ((dp[i-1][k]) % 10007)
        dp[i][d] = total

print(sum(dp[N]) % 10007)