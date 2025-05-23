import sys
input = sys.stdin.readline

n = int(input().strip())

cnt = 0
k = 1

while k * k <= n:
    cnt += 1
    k += 1

print(cnt)
