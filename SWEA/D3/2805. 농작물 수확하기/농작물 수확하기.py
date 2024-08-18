T = int(input())

for tc in range(1, T+1):
    N = int(input())
    crops = [list(map(int, input())) for _ in range(N)]
    M = N // 2 # 중앙 인덱스
    ans = 0

    for i in range(N):
        if i <= M:
            for j in range(M - i, M + i + 1):
                ans += crops[i][j]
        else:
            for k in range(i - M, N -(i - M)):
                ans += crops[i][k]
    print(f'#{tc} {ans}')