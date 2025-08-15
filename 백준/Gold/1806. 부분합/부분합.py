import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
sum_num = nums[0]
ans = None

while left <= right < N:
    if sum_num >= S:
        if ans is None or ans > right - left + 1:
            ans = right - left + 1
        sum_num -= nums[left]
        left += 1
    else:
        right += 1
        if right < N:
            sum_num += nums[right]

print(0 if ans is None else ans)
