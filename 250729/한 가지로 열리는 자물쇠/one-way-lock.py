N = int(input())
a, b, c = list(map(int, input().split()))
cnt = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if i + 2 <= a or i - 2 <= a\
            or j + 2 <= b or j - 2 <= b\
            or k + 2 <= c or k - 2 <= c:
                cnt += 1

print(cnt)
