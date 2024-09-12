T = int(input())
for _ in range(T):
    C = int(input())
    coins = [0] * 4

    while C > 0:
        if C >= 25:
            C -= 25
            coins[0] += 1
        elif C >= 10:
            C -= 10
            coins[1] += 1
        elif C >= 5:
            C -= 5
            coins[2] += 1
        else:
            C -= 1
            coins[3] += 1
    print(*coins)