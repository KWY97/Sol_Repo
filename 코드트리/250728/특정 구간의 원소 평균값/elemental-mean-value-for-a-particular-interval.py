N = int(input())
numbers = list(map(int, input().split()))
cnt = 0

for i in range(N):
    for j in range(i, N):
        temp = 0
        for k in range(i, j+1):
            temp += numbers[k]

        average = temp / (j - i + 1)
        if average in numbers[i:j+1]:
            cnt += 1

print(cnt)