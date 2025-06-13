def d_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def my_game(n, k, board, horse):
    game_turn = 1
    horse_stack = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(k):
        r, c, d = horse[i]
        horse[i] = [r - 1, c - 1, d - 1]
        horse_stack[r - 1][c - 1].append(i)

    while game_turn <= 1000:
        for i in range(k):
            r, c, d = horse[i]
            new_r, new_c = r + dr[d], c + dc[d]
            moving_horses = []

            if not 0 <= new_r < n or not 0 <= new_c < n or board[new_r][new_c] == 2:
                new_d = d_go_back(d)
                horse[i][2] = new_d
                new_r, new_c = r + dr[new_d], c + dc[new_d]
                if not 0 <= new_r < n or not 0 <= new_c < n or board[new_r][new_c] == 2:
                    continue

            for j in range(len(horse_stack[r][c])):
                current_stacked_horse = horse_stack[r][c][j]
                if i == current_stacked_horse:
                    moving_horses = horse_stack[r][c][j:]
                    horse_stack[r][c] = horse_stack[r][c][:j]
                    break

            if board[new_r][new_c] == 1:
                moving_horses = moving_horses[::-1]

            for moving_horse in moving_horses:
                horse_stack[new_r][new_c].append(moving_horse)
                horse[moving_horse][0], horse[moving_horse][1] = new_r, new_c

            if len(horse_stack[new_r][new_c]) >= 4:
                return game_turn

        game_turn += 1
    return -1



N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
horse = [list(map(int, input().split())) for _ in range(K)]
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

print(my_game(N, K, board, horse))