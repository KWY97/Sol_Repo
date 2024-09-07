size = 100
arr = [[0] * size for _ in range(size)]
ans = 0

N = int(input())
for _ in range(N):
    start_x, start_y = map(int, input().split())
    end_x, end_y = start_x + 10, start_y + 10
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            arr[i][j] = 1
for i in range(size):
    ans += arr[i].count(1)
print(ans)