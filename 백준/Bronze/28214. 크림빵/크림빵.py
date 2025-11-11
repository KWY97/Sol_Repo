N, K, P = map(int, input().split())
breads = list(map(int, input().split()))
cnt = 0
ans = 0

for i in range(N * K):
    if breads[i] == 0:
        cnt += 1

    if (i+1) % K == 0:
        if cnt < P:
            ans += 1
        cnt = 0

print(ans)
