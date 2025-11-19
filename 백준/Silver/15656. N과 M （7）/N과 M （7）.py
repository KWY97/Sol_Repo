def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(N):
        s.append(nums[i])
        dfs()
        s.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []
dfs()