import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)
stack = []
ans = 0

for i in range(n):
    if s[i] == '(':
        stack.append('(')
    else:
        if s[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1

print(ans)

