import sys
input = sys.stdin.readline

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        s.append(nums[i])
        dfs()
        s.pop()
        used[i] = False


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
used = [False] * N
s = []

dfs()