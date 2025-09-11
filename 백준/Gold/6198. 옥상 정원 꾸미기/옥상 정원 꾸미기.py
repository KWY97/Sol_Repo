N = int(input())
buildings = [int(input()) for _ in range(N)]
ans = 0
stack = []

for i, v in enumerate(buildings):
    while stack and stack[-1] <= v:
        stack.pop()
    ans += len(stack)
    stack.append(v)

print(ans)