N = int(input())
num = list(map(int, input().split()))
v = int(input())
cnt = 0

for x in num:
    if x == v:
        cnt += 1

print(cnt)