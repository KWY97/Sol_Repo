N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
start = 0
end = 0
temp = nums[0]

while end < N:
    if temp == M:
        cnt += 1

    if temp >= M:
        temp -= nums[start]
        start += 1
    else:
        end += 1
        if end < N:
            temp += nums[end]

print(cnt)