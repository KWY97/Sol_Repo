import sys
input = sys.stdin.readline

ans = ['factor', 'multiple', 'neither']

while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    if B % A == 0:
        print(ans[0])
    elif A % B == 0:
        print(ans[1])
    else:
        print(ans[2])