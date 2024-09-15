import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
cnt = 0

for num in arr:
    temp = []
    for i in range(1, num):
        if num % i == 0:
            temp.append(i)
    if len(temp) == 1:
        cnt += 1
print(cnt)