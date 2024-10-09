import sys
input = sys.stdin.readline


x = int(input())

li = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

for i in range(len(li)):
    if x >= li[i]:
        cnt += 1
        x -= li[i]

    if x == 0:
        break
print(cnt)
