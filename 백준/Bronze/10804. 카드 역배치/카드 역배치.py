nums = [i for i in range(1, 21)]

for _ in range(10):
    s, e = map(int, input().split())
    s -= 1
    e -= 1

    temp = nums[:s] + nums[s:e+1][::-1] + nums[e+1:]
    nums = temp

print(' '.join(map(str, nums)))