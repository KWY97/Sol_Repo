N = int(input())
mine_arr = [list(input()) for _ in range(N)]
dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
result = []

for x in range(N):
    temp = []
    for y in range(N):
        if mine_arr[x][y] != '.':
            temp.append('*')
        else:
            cnt = 0

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if mine_arr[nx][ny] != '.':
                    cnt += int(mine_arr[nx][ny])

            if cnt >= 10:
                temp.append('M')
            else:
                temp.append(str(cnt))
    result.append(temp)

for i in result:
    print(''.join(i))