from collections import defaultdict

N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums_dic = defaultdict(int)

start = 0
end = 0
ans = 0

while end < N:
    if nums_dic[nums[end]] < K:
        nums_dic[nums[end]] += 1
        end += 1
    else:
        nums_dic[nums[start]] -= 1
        start += 1

    ans = max(end-start, ans)
print(ans)
