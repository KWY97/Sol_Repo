from collections import deque

def rotate_to_clean(d):
    return (d + 3) % 4

def go_to_back(d):
    return (d + 2) % 4

def clean_room(r, c, d, n, m, room):
    room_cnt = 1
    room[r][c] = 2
    queue = deque([[r, c, d]])

    while queue:
        r, c, d = queue.popleft()
        temp_d = d

        for i in range(4):
            temp_d = rotate_to_clean(temp_d)
            new_r, new_c = r + dxy[temp_d][0], c + dxy[temp_d][1]

            if  0 <= new_r < n and 0 <= new_c < m and room[new_r][new_c] == 0:
                room_cnt += 1
                room[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break


            elif i == 3:
                temp_d = go_to_back(d)
                new_r, new_c = r + dxy[temp_d][0], c + dxy[temp_d][1]
                if room[new_r][new_c] == 1:
                    return room_cnt
                queue.append([new_r, new_c, d])

    return room_cnt


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북: 0, 동: 1, 남: 2, 서: 3
print(clean_room(r, c, d, N, M, room))