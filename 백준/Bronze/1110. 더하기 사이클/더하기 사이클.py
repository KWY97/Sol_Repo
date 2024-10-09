import sys
input = sys.stdin.readline

N = int(input())
original = N
cnt = 0

while True:
    a = N % 10
    b = N // 10
    c = (a + b) % 10
    N = (a * 10) + c

    cnt += 1

    if N == original:
        break

print(cnt)


