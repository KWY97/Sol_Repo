nums = list(map(int, input()))

if len(nums) == 2:
    print(nums[0] + nums[1])
elif len(nums) == 3:
    if nums[0] == 1 and nums[1] == 0:
        print(10 + nums[2])
    else:
        print(nums[0] + 10)
else:
    print(20)