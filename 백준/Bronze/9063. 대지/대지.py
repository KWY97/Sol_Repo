import sys
input = sys.stdin.readline

N = int(input())
max_y = -9999
min_y = 10001

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if max_y < arr[i][1]:
        max_y = arr[i][1]
    if min_y > arr[i][1]:
        min_y = arr[i][1]

max_x = ((max(arr))[0]) # x 좌표 제일 큰 놈 나옴
min_x = ((min(arr))[0]) # x 좌표 제일 작은 놈 나옴

print((max_x - min_x) * (max_y - min_y))
