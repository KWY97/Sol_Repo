a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

if a == b or a + 1 == b:
    print(0)
else:
    print(b - a - 1)
    print(' '.join(str(i) for i in range(a+1, b)))
