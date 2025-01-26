N = int(input())
start = 666
cnt = 0

while True:
    if cnt == N:
        break

    if '666' in str(start):
        cnt += 1
    start += 1

print(start - 1)