n = int(input())
rooms =[int(input()) for _ in range(n)]
min_dist = None

for i in range(n):
    temp_dist = 0
    for j in range(n):
        diff = (j - i + n) % n
        temp_dist += (diff * rooms[j])

    if min_dist is None or min_dist > temp_dist:
        min_dist = temp_dist

print(min_dist)