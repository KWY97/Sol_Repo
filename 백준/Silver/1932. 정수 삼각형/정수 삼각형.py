n = int(input())
dp =[]

for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        # 제일 처음
        if j == 0:
            dp[i][j] += dp[i-1][j]
        # 제일 끝
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        # 보통 경우
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))