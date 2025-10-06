t = []
for _ in range(2):
    a, b, c, d, e = map(int, input().split())
    a *= 6
    b *= 3
    c *= 2
    e *= 2

    ans = a+b+c+d+e
    t.append(ans)
print(' '.join(map(str, t)))