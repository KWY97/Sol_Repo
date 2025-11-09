N = int(input())
nums = list(map(int, input().split()))
dp = [-1001] * N
dp[0] = nums[0]

for i in range(1, N):
    prefix_sum = dp[i-1] + nums[i]

    if prefix_sum < nums[i]:
        dp[i] = nums[i]
    else:
        dp[i] = prefix_sum

print(max(dp))
