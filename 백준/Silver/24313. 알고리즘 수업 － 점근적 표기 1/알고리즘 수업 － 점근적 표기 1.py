a1, a2 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 <= c and a1 * n0 + a2 <= c * n0:
    print(1)
else:
    print(0)