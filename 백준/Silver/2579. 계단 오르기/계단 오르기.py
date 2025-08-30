n = int(input())
steps = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)
dp[1] = steps[1]

if n >= 2:
    dp[2] = steps[1] + steps[2]

for i in range(3, n+1):
    dp[i] = max(
        dp[i-2] + steps[i],
        dp[i-3] + steps[i-1] + steps[i]
    )

print(dp[n])