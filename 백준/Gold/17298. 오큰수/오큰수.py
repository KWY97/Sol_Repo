import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip().split()))
stack = []
ans = [0] * N

for i, v in enumerate(nums):
    if not stack:
        stack.append([i, v])
    else:
        while stack and stack[-1][1] < v:
            pop_i, _ = stack.pop()
            ans[pop_i] = v
        stack.append([i, v])

for j in range(N):
    if ans[j] == 0:
        ans[j] = -1

print(' '.join(map(str, ans)))