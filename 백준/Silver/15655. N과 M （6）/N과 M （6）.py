def dfs(n):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(n, N):
        s.append(nums[i])
        dfs(i+1)
        s.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
dfs(0)