def fac(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]
    return dp[n]

n, k = map(int, input().split())
p = 1

for _ in range(k):
    p *= n
    n -= 1

c = fac(k)

print(p // c)