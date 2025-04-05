x, y = map(int, input().split())
ans = 1000 * x / y
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if ans > ((1000 * a) / b):
        ans = ((1000 * a) / b)
print(round(ans, 2))