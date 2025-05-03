import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = []

see = [input().strip() for _ in range(n)]
listen = set(input().strip() for _ in range(m))

for i in see:
    if i in listen:
        ans.append(i)

ans.sort()

print(len(ans))
print("\n".join(ans))