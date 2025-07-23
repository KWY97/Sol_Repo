def to_decimal(li_num, length):
    decimal = 0
    for i in range(length):
        decimal = 2 * decimal + li_num[i]
    return decimal

a = list(map(int, input()))
n = len(a)
ans = 0

for i in range(n):
    a[i] = 1 - a[i]
    ans = max(ans, to_decimal(a, n))
    a[i] = 1 - a[i]

print(ans)