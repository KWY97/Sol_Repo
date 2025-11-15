import sys
input = sys.stdin.readline

N, S = map(int, input().split())
car_x = list(map(int, input().split()))
car_h = list(map(int, input().split()))
S -= 1

# S기준 도달 가능 구간 (좌, 우)
l = car_x[S] - car_h[S]
r = car_x[S] + car_h[S]

# 왼쪽으로 가장 치우친 차의 인덱스
low = S
# 오른쪽으로 가장 치우친 차의 인덱스
high = S

while True:
    new_l = l
    new_r = r

    i = low - 1
    while i >= 0 and car_x[i] >= l:
        new_l = min(new_l, car_x[i] - car_h[i])
        new_r = max(new_r, car_x[i] + car_h[i])
        low = i
        i -= 1

    i = high + 1
    while i < N and car_x[i] <= r:
        new_l = min(new_l, car_x[i] - car_h[i])
        new_r = max(new_r, car_x[i] + car_h[i])
        high = i
        i += 1

    if l == new_l and r == new_r:
        break

    l = new_l
    r = new_r

ans = []
for i in range(low, high+1):
    ans.append(str(i+1))

print(' '.join(ans))