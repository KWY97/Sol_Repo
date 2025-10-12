def fibo(n):
    if n in memo:
        return memo[n]

    for i in range(2, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 1000000000

    return memo[n]


memo = {
    0: 0,
    1: 1
}

N = int(input())
ans = fibo(abs(N))

if N == 0:
    print(0)
    print(ans)
elif (N < 0) and (N % 2 == 0):
    print(-1)
    print(ans)
elif (N < 0) and (N % 2 != 0):
    print(1)
    print(ans)
else:
    print(1)
    print(ans)
