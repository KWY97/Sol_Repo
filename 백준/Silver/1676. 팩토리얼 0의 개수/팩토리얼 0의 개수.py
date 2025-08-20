def fac(n):
    if n in dp:
        return dp[n]
    else:
        for i in range(3, n+1):
            dp[i] = i * dp[i-1]
    return dp[n]

dp = {
    0: 1,
    1: 1,
    2: 2
}

N = int(input())
num = str(fac(N))
cnt = 0

for char in num[::-1]:
    if char == '0':
        cnt += 1
    else:
        print(cnt)
        break