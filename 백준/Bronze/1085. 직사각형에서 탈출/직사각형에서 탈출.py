import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

ans_x = 0
ans_y = 0
ans = 0

if x > w-x:
    ans_x = w-x
else:
    ans_x = x

if y > h-y:
    ans_y = h-y
else:
    ans_y = y

if ans_x > ans_y:
    ans = ans_y
else:
    ans = ans_x

print(ans)