def back(start, seq):
    if len(seq) == M:
        print(*seq)
        return

    for i in range(start, N):
        back(i, seq + [nums[i]])


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
back(0, [])