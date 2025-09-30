N = int(input())
nums = list(map(int, input().split()))
ans = [False] * N
cnt = 0

while True:
    s = min(nums)
    if s == 1001:
        break

    for i, v in enumerate(nums):
        if v == s and ans[i] == False:
            ans[i] = cnt
            cnt += 1
            nums[i] = 1001
            break

print(' '.join(map(str, ans)))