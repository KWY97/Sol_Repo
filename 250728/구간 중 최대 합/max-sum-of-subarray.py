n, k = map(int, input().split())
numbers = list(map(int, input().split()))
ans = None

for i in range(n-k+1):
    temp_sum = numbers[i]
    for j in range(i+1, i+k):
        temp_sum += numbers[j]

    if ans is None or ans < temp_sum:
        ans = temp_sum

print(ans)