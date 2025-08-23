from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    imps = list(map(int, input().split()))
    q = deque()

    for i in range(N):
        if i == M:
            q.append([imps[i], True])
        else:
            q.append([imps[i], False])

    cnt = 0
    while q:
        imp, check = q.popleft()
        is_biggest = True

        for j in range(len(q)):
            if q[j][0] > imp:
                is_biggest = False
                break

        if not is_biggest:
            q.append([imp, check])
        else:
            cnt += 1
            if check:
                print(cnt)
                break