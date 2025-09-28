N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

m, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

ans = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            ans[i][j] += A[i][k] * B[k][j]
for line in ans:
    print(' '.join(map(str, line)))