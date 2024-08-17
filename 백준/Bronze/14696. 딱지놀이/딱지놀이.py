N = int(input()) # 라운드 수

for _ in range(N):
    game_A = (list(map(int, input().split())))[1:]
    game_B = (list(map(int, input().split())))[1:]

    for i in range(4, 0, -1):
        if game_A.count(i) > game_B.count(i):
            print('A')
            break
        elif game_A.count(i) < game_B.count(i):
            print('B')
            break
        if i == 1:
            print('D')