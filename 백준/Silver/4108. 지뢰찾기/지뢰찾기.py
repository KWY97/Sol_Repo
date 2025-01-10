from pprint import pprint

dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break

    mine_arr = [list(input()) for _ in range(n)]
    result = []

    for x in range(n):
        temp = []
        for y in range(m):
            if mine_arr[x][y] == '*':
                temp.append('*')
            else:
                cnt = 0
                for dx, dy in dxy:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if mine_arr[nx][ny] == '*':
                        cnt += 1

                temp.append(str(cnt))
        result.append(temp)

    for i in range(n):
        print(''.join(result[i]))