n = int(input())
towers = list(map(int, input().split()))
stack = []
ans = 0


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


if stack:
    ans += 1

print(ans)