def concave(N):
    for i in range(N):
        for j in range(N):
            for k in range(4): # 4개의 방향
                cnt = 0
                ni, nj = i, j # 현재 위치부터 돌인지 판단
                while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    ni += dxy[k][0]
                    nj += dxy[k][1]
    return 'NO'
                    
dxy = [[0, 1], [1, 1], [1, 0], [1, -1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = concave(N)
    print(f'#{tc} {ans}')