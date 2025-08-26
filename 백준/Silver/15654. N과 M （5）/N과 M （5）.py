def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(N):
        if not used[i]:
            s.append(nums[i])
            used[i] = True
            dfs()
            s.pop()
            used[i] = False



N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
used = [False] * N
s = []
dfs()