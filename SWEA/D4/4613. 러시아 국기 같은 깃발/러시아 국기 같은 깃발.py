T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    sum = float('-inf')
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for w in range(i+1):
                cnt += arr[w].count('W')
            for b in range(i+1, j+1):
                cnt += arr[b].count('B')
            for r in range(j+1, N):
                cnt += arr[r].count('R')
                
            sum = max(sum, cnt)

    print(f'#{tc} {N*M - sum}')