N = int(input())
numbers = list(map(int, input().split()))
ans = 0

for i in range(N-2):
    # print('-------------')
    for j in range(i+2, N):
        # print(f'i={i}, j={j}, sum={numbers[i] + numbers[j]}')
        ans = max(ans, numbers[i] + numbers[j])

print(ans)
