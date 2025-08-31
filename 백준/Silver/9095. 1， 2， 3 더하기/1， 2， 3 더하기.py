T = int(input())

for _ in range(T):
    n = int(input())
    # dp[i] = 정수 i를 1, 2, 3 의 합으로 나타내는 방법의 수
    dp = [0] * (max(4, n+1))

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])