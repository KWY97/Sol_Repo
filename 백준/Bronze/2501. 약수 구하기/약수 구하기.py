import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0
flag = 1

for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
        if cnt == K:
            flag = 0
            print(i)
if flag == 1:
    print(0)