day = int(input())
cars = map(int, input().split())
cnt = 0

for car in cars:
    if car == day:
        cnt += 1
print(cnt)