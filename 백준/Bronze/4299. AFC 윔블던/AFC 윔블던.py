import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A + B < 0 or A - B < 0:
    print(-1)
else:
    C = (A + B) // 2
    D = A - C
    if (C+D) == A and (C-D) == B:
        print(C, D)
    else:
        print(-1)