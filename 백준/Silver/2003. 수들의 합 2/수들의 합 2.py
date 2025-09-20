N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
start = 0
end = 0

while end < N:
    temp = sum(nums[start:end+1])

    if temp == M:
        cnt += 1
        end += 1
    elif temp > M:
        start += 1
    else:
        end += 1

print(cnt)