from collections import deque

def turn_left(d):
    return (d + 3) % 4

def turn_back(d):
    return (d + 2) % 4

def clean_room(r, c, d, my_map, n, m):
    room_cnt = 1
    my_map[r][c] = 2
    queue = deque()
    queue.append([r, c, d])

    while queue:
        r, c, d = queue.popleft()
        temp_d = d

        for i in range(4):
            temp_d = turn_left(temp_d)
            next_r, next_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= next_r < n and 0 <= next_c < m and my_map[next_r][next_c] == 0:
                room_cnt += 1
                my_map[next_r][next_c] = 2
                queue.append([next_r, next_c, temp_d])
                break
            elif i == 3:
                temp_d = turn_back(d)
                next_r, next_c = r + dr[temp_d], c + dc[temp_d]
                if my_map[next_r][next_c] == 1:
                    return room_cnt
                queue.append([next_r, next_c, d])
    return room_cnt



N, M = map(int, input().split())
r, c, d = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

print(clean_room(r, c, d, my_map, N, M))