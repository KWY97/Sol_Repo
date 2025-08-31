n = int(input())

#dp[i] = 2*i 직사각형을 채우는 방법의 수
dp = [0] * max(4 ,n+1)
dp[1] = 1
dp[2] = 3
dp[3] = 5

for i in range(4, n+1):
    dp[i] = (dp[i-1] + (2 * dp[i-2])) % 10007

print(dp[n] % 10007)