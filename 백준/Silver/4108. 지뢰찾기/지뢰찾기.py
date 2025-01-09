while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    arr = [list(input()) for _ in range(n)]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    ans = []
    for x in range(n):
        temp = []
        for y in range(m):
            cnt = 0
            if arr[x][y] == "*":
                temp.append("*")
            else:
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] == "*":
                            cnt += 1
                temp.append(str(cnt))
        ans.append(temp)

    for i in ans:
        print(''.join(i))