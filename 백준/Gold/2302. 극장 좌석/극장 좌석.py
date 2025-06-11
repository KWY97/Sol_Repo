def precompute_fibo(n):
    dp = {0: 1, 1: 1}
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp

def cnt_seat(n, fix_seats):
    ans = 1
    cnt = 0
    for i in range(1, n+1):
        if i not in fix_seats:
            cnt += 1
            if i == n:
                ans *= dp[cnt]
        else:
            ans *= dp[cnt]
            cnt = 0
    return ans

N = int(input())
M = int(input())
fix_seats = []

for _ in range(M):
    fix_seat = int(input())
    fix_seats.append(fix_seat)
fix_seats = set(fix_seats)
dp = precompute_fibo(N)
print(cnt_seat(N, fix_seats))