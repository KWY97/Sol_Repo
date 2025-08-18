import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
dp = []
prefix_sum = 0

for num in nums:
    prefix_sum += num
    dp.append(prefix_sum)

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(dp[j-1])
    else:
        print(dp[j-1] - dp[i-2])