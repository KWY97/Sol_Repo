N = int(input())
nums = list(map(int, input().split()))
nums.sort()

left = 0
right = N-1

ans = abs(nums[left] + nums[right])
result = [nums[left], nums[right]]

while left < right:
    temp = nums[left] + nums[right]

    if ans >= abs(temp):
        ans = abs(temp)
        result = [nums[left], nums[right]]
        if ans == 0:
            break

    if temp < 0:
        left += 1
    elif temp > 0:
        right -= 1


print(result[0], result[1])