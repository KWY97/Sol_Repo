def turn_right(d):
    return (d + 1) % 4

def turn_left(d):
    return (d + 3) % 4

n = int(input())
moves = input()
dr = [1, 0, -1, 0] # 남, 서, 북, 동
dc = [0, -1, 0, 1]
r, c, d = 0, 0, 0
visited = {(r, c)}

for move in moves:
    if move == 'R':
        d = turn_right(d)
    elif move == 'L':
        d = turn_left(d)
    elif move == 'F':
        r = r + dr[d]
        c = c + dc[d]
        visited.add((r, c))

min_r = min(r for r, _ in visited)
max_r = max(r for r, _ in visited)
min_c = min(c for _, c in visited)
max_c = max(c for _, c in visited)

for rr in range(min_r, max_r + 1):
    line = []
    for cc in range(min_c, max_c + 1):
        if (rr, cc) in visited:
            line.append('.')
        else:
            line.append('#')
    print(''.join(line))