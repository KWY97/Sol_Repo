N, M = map(int, input().split())

s_list = [input() for _ in range(N)]
check_list = [input() for _ in range(M)]

cnt = 0

for check in check_list:
    if check in s_list:
        cnt += 1

print(cnt)