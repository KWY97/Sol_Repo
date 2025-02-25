ans_li = ['E', 'A', 'B', 'C', 'D']
arr = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    cnt = 0
    for j in range(4):
        if arr[i][j] == 1: continue
        cnt += 1
    print(ans_li[cnt])