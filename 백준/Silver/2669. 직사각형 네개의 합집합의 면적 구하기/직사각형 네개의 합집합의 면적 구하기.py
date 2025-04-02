my_map = [[0] * 101 for _ in range(101)]
cnt = 0

for _ in range(4):
    a, b, c, d = map(int, input().split())

    for i in range(a+1, c+1):
        for j in range(b+1, d+1):
            my_map[i][j] = 1


for i in range(101):
    for j in range(101):
        if my_map[i][j] == 1:
            cnt += 1

print(cnt)