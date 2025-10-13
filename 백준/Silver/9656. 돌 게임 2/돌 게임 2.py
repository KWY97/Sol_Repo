def dp(n):
    if n in memo:
        return memo[n]
    for i in range(3, n+1):
        memo[i] = memo[i-2]
    return memo[n]

N = int(input())
memo = {
    1: 'CY',
    2: 'SK'
}
print(dp(N))
