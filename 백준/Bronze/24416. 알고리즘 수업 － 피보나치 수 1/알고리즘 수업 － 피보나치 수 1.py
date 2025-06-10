def fibonacci(n):
    dp = [0] * (n+2)
    dp[1], dp[2] = 1, 1
    cnt = 0

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt += 1

    return [dp[n], cnt]

n = int(input())
print(*fibonacci(n))