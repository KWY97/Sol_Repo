A, B = map(int, input().split())

max_a = A // 2

if max_a == 0:
    print(0)
elif max_a < B:
    print(max_a)
else:
    print(B)
