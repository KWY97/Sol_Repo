T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 행 검사
    for i in range(N):
        row_cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                row_cnt += 1
            else:
                if row_cnt == K:
                    cnt += 1
                row_cnt = 0
        if row_cnt == K:
            cnt += 1

    # 열 검사
    for i in range(N):
        col_cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                col_cnt += 1
            else:
                if col_cnt == K:
                    cnt += 1
                col_cnt = 0
        if col_cnt == K:
            cnt += 1

    print(f'#{tc} {cnt}')