import sys
input = sys.stdin.readline

n = int(input())

commute = {}
ans = []

for _ in range(n):
    name, status = input().split()
    commute[name] = status

for x in commute:
    if commute[x] == "enter":
        ans.append(x)

ans.sort(reverse=True)

for y in ans:
    print(y)