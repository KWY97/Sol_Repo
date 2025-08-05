import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    if K >= 63:
        print(0)
        continue

    temp1 = N // (2 ** K)
    temp2 = N // (2 ** (K + 1))

    print(temp1 - temp2)