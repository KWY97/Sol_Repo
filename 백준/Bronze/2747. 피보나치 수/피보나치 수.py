def fibo(n):
    memo = {0: 0, 1: 1, 2: 1}

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]


    return memo[n]

print(fibo(int(input())))