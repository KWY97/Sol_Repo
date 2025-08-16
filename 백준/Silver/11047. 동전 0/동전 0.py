N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
cnt = 0

for coin in coins:
    if K == 0:
        break

    if coin > K:
        continue
    else:
        cnt += K // coin
        K %= coin

print(cnt)