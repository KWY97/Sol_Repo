import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip().split()))
stack = []
ans = [-1] * N

for i, v in enumerate(nums):
    while stack and nums[stack[-1]] < v:
        ans[stack.pop()] = v
    stack.append(i)
print(' '.join(map(str, ans)))