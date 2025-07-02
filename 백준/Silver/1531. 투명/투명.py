def get_mosaic(li):
    cnt = 0
    for i in range(100):
        for j in range(100):
            if li[i][j] > M:
                cnt += 1
    return cnt


N, M = map(int, input().split())
my_map = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            if my_map[i][j] > M:
                continue
            my_map[i][j] += 1

print(get_mosaic(my_map))