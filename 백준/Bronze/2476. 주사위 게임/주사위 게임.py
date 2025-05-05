import sys
input = sys.stdin.readline

n = int(input().strip())
ans = 0

for _ in range(n):
    a, b, c = map(int, input().strip().split())

    # 3개가 같은 경우
    if (a == b) and (b == c):
        price = 10000 + a * 1000
    # 2개가 같은 경우
    elif (a == b) or (b == c):
        price = 1000 + b * 100
    elif (a == c):
        price = 1000 + a * 100
    # 모두 다른 경우
    else:
        price = (max(a, b, c) * 100)

    if ans < price:
        ans = price

print(ans)