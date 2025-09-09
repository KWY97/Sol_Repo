import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = []
ans = 1

for tower in towers:
    if not stack:
        stack.append(tower)
    else:
        if stack[-1] <= tower:
            while stack and (stack[-1] <= tower):
                stack.pop()
            stack.append(tower)
            ans += 1
        else:
            stack.append(tower)

print(ans)