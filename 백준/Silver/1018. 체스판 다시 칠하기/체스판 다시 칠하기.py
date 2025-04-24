n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = []

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0 # 맨 왼쪽 위칸이 B로 설정
        draw2 = 0 # 맨 왼쪽 위칸을 W로 설정

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if board[x][y] != "B":
                        draw1 += 1
                    else:
                        draw2 += 1
                else:
                    if board[x][y] != "W":
                        draw1 += 1
                    else:
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))