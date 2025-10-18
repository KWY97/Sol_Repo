def rotate(gear, direction):
    if direction == 1:
        return gear[-1] + gear[:-1]
    else:
        return gear[1:] + gear[0]

cogs = [input().strip() for _ in range(4)]

K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    n -= 1

    rotate_dir = [0] * 4
    rotate_dir[n] = d

    # 왼쪽
    for i in range(n - 1, -1, -1):
        if cogs[i][2] != cogs[i + 1][6]:
            rotate_dir[i] = -rotate_dir[i + 1]
        else:
            break

    # 오른쪽
    for i in range(n + 1, 4):
        if cogs[i - 1][2] != cogs[i][6]:
            rotate_dir[i] = -rotate_dir[i - 1]
        else:
            break

    for i in range(4):
        if rotate_dir[i] != 0:
            cogs[i] = rotate(cogs[i], rotate_dir[i])

ans = 0
for i in range(4):
    if cogs[i][0] == '1':
        ans += 2**i

print(ans)