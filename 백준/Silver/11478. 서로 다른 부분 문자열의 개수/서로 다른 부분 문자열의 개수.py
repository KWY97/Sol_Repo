import sys
input = sys.stdin.readline

s = input().strip()
ans = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        ans.add(s[i:j+1])

print(len(ans))